import json
from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title="GameVault",page_icon="🎮",layout="wide")
DATA=Path("gamevault_data.json")
st.markdown("""<style>.stApp{background:#080a0f}.block-container{max-width:1200px;padding-top:2rem}[data-testid="stMetric"]{background:#10141d;border:1px solid #262e3a;padding:16px;border-radius:12px}</style>""",unsafe_allow_html=True)

def load():
    if DATA.exists():
        try:return json.loads(DATA.read_text(encoding="utf-8"))
        except Exception:pass
    return [
      {"title":"Elden Ring","platform":"PC","status":"Playing","genre":"Action RPG","hours":62.0,"rating":9.5,"achievements":28,"favorite":True,"notes":"Exploring the Lands Between."},
      {"title":"Hades","platform":"PC","status":"Completed","genre":"Roguelike","hours":44.0,"rating":9.0,"achievements":36,"favorite":True,"notes":"Completed the main story."},
      {"title":"Minecraft","platform":"PC","status":"Playing","genre":"Sandbox","hours":180.0,"rating":9.0,"achievements":21,"favorite":False,"notes":"Long-term survival world."}
    ]
def save():DATA.write_text(json.dumps(st.session_state.games,indent=2),encoding="utf-8")
if "games" not in st.session_state:st.session_state.games=load()

st.title("🎮 GameVault")
st.caption("Your personal gaming history, library, and stats — built in Python.")
tab1,tab2,tab3,tab4=st.tabs(["Dashboard","My Games","Add / Edit","Stats"])

with tab1:
    games=st.session_state.games
    hours=sum(float(g["hours"]) for g in games);completed=sum(g["status"]=="Completed" for g in games);avg=sum(float(g["rating"]) for g in games)/len(games) if games else 0
    a,b,c,d=st.columns(4);a.metric("Games tracked",len(games));b.metric("Total playtime",f"{hours:.1f} h");c.metric("Completed",completed);d.metric("Average rating",f"{avg:.1f}/10")
    st.subheader("Currently playing")
    playing=[g for g in games if g["status"]=="Playing"]
    if not playing:st.info("Nothing marked Playing yet.")
    for g in playing:
        with st.container(border=True):
            x,y,z=st.columns([4,1,1]);x.markdown(f"### {'⭐ ' if g.get('favorite') else ''}{g['title']}");x.caption(f"{g['platform']} • {g['genre']}");y.metric("Playtime",f"{g['hours']} h");z.metric("Rating",f"{g['rating']}/10")

with tab2:
    q=st.text_input("Search library").lower();status=st.selectbox("Status filter",["All","Playing","Completed","Backlog","Dropped"])
    filtered=[g for g in st.session_state.games if (not q or q in (g["title"]+" "+g["genre"]+" "+g["platform"]).lower()) and (status=="All" or g["status"]==status)]
    for i,g in enumerate(filtered):
        with st.expander(f"{'⭐ ' if g.get('favorite') else ''}{g['title']} — {g['status']}"):
            st.write(f"**Platform:** {g['platform']}  |  **Genre:** {g['genre']}  |  **Playtime:** {g['hours']} h  |  **Rating:** {g['rating']}/10")
            st.write(g.get("notes") or "No notes.")
            c1,c2,c3=st.columns(3)
            if c1.button("+1 hour",key=f"h1{i}"):
                g["hours"]=round(float(g["hours"])+1,1);save();st.rerun()
            if c2.button("Favorite / unfavorite",key=f"fav{i}"):
                g["favorite"]=not g.get("favorite",False);save();st.rerun()
            if c3.button("Delete",key=f"delete{i}"):
                st.session_state.games.remove(g);save();st.rerun()

with tab3:
    st.subheader("Add a game")
    with st.form("add"):
        title=st.text_input("Title");c1,c2=st.columns(2);platform=c1.selectbox("Platform",["PC","PlayStation","Xbox","Switch","Other"]);status=c2.selectbox("Status",["Backlog","Playing","Completed","Dropped"])
        genre=st.text_input("Genre");c3,c4,c5=st.columns(3);hours=c3.number_input("Playtime",0.0,10000.0,0.0,.5);rating=c4.number_input("Rating",0.0,10.0,0.0,.5);ach=c5.number_input("Achievements",0,10000,0);fav=st.checkbox("Favorite");notes=st.text_area("Notes")
        if st.form_submit_button("Add to GameVault",type="primary"):
            if title.strip():
                st.session_state.games.append({"title":title.strip(),"platform":platform,"status":status,"genre":genre.strip() or "Unknown","hours":hours,"rating":rating,"achievements":ach,"favorite":fav,"notes":notes.strip()});save();st.success("Game added.")
            else:st.error("Enter a title.")
    st.subheader("Edit a game")
    if st.session_state.games:
        choice=st.selectbox("Choose game",[g["title"] for g in st.session_state.games],key="editpick");g=next(x for x in st.session_state.games if x["title"]==choice)
        with st.form("edit"):
            e_status=st.selectbox("Status",["Backlog","Playing","Completed","Dropped"],index=["Backlog","Playing","Completed","Dropped"].index(g["status"]));e_hours=st.number_input("Playtime",0.0,10000.0,float(g["hours"]),.5);e_rating=st.number_input("Rating",0.0,10.0,float(g["rating"]),.5);e_notes=st.text_area("Notes",g.get("notes",""))
            if st.form_submit_button("Save changes"):
                g.update(status=e_status,hours=e_hours,rating=e_rating,notes=e_notes);save();st.success("Changes saved.")

with tab4:
    if st.session_state.games:
        df=pd.DataFrame(st.session_state.games)
        c1,c2=st.columns(2)
        with c1:st.subheader("Hours by status");st.bar_chart(df.groupby("status")["hours"].sum())
        with c2:st.subheader("Games by platform");st.bar_chart(df["platform"].value_counts())
        st.subheader("Highest rated");st.dataframe(df.sort_values("rating",ascending=False)[["title","platform","status","hours","rating","achievements"]],use_container_width=True,hide_index=True)
    else:st.info("Add games to unlock stats.")

st.divider()
backup=json.dumps(st.session_state.games,indent=2)
st.download_button("Export library backup",backup,"gamevault-backup.json","application/json")
upload=st.file_uploader("Restore JSON backup",type="json")
if upload and st.button("Restore backup"):
    try:
        data=json.load(upload)
        if not isinstance(data,list):raise ValueError()
        st.session_state.games=data;save();st.success("Backup restored.");st.rerun()
    except Exception:st.error("That backup is not valid.")
