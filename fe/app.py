#pip install streamlit 
#python -m pip install steamlit
#py -m pip install streamlit 
#running comand streamlit run app.py
import streamlit as st
import requests as r 
st.title("AI TRAVEL PLANNER")
st.subheader("enter all trip data")
starting_loc=st.text_input("Enter Starting Location")
destination_loc=st.text_input("Enter Destination Location")
no_of_trip_days=st.number_input("Enter Trip Days", min_value=1)
no_of_people=st.number_input("Enter Number of People Count", min_value=1)
budget=st.number_input("Enter Budget", min_value=10000, max_value=100000, step=10000)
specifications=st.text_area("Enter Your Specifications", placeholder="Example:--party,places,temples etc..")
btn=st.button("BuildTravellingPlan")
if btn:
    payload={
        "starting_loc":starting_loc,
        "destination_loc":destination_loc,
        "no_of_trip_days":no_of_trip_days,
        "no_of_people":no_of_people,
        "budget":budget,
        "specifications":specifications
    }
    be_res=r.post("http://127.0.0.1:8000/plan_trip",json=payload)
    if be_res.status_code==200:
        st.write(be_res.json()["travel_plan"])
        
