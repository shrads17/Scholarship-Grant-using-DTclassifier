import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

model = pickle.load(open('Dt.pkl','rb'))

def clf(edu,Gen,Ex,Dis,Ann,In,India): # education qualicatoion Gender Exservice Disability Income
    input = pd.DataFrame(np.array([edu,Gen,Ex,Dis,Ann,In,India]).reshape(1,-1),columns= ['edu','Gen','Ex','Dis','Ann','In','India'])
    prediction = model.predict(input)
    return float(prediction)

def edu_normal(edu):
    if edu == 'UG':
        edu = 0
    elif edu == 'PG':
        edu = 1
    elif edu == 'Dr.':
        edu = 2
    elif edu == 'Select':
        st.write('Select Education Again')
    return edu

def Gen_normal(Gen):
    if Gen == 'Male':
        Gen = 1
    elif Gen == 'Female':
        Gen = 0
    elif Gen == 'Select':
        st.write('Select Gender Again')
    return Gen

def Ex_normal(Ex):
    if Ex == 'Yes':
        Ex = 1
    elif Ex == 'No':
        Ex = 0
    elif Ex == 'Select':
        st.write('Select Service Again')
    return Ex

def Dis_normal(Dis):
    if Dis == 'Yes':
        Dis = 1
    elif Dis == 'No':
        Dis = 0
    elif Dis == 'Select':
        st.write('Select Disability Status Again')
    return Dis

def na_normal(India):
    if India == 'Yes':
        India = 1
    elif India == 'No':
        India = 0
    elif India == 'Select':
        st.write('Select Nationality Again')
    return India

def Ann_normal(Ann):
    if Ann == '90-100':
        Ann = 0
    elif Ann == '80-90':
        Ann = 1
    elif Ann == '70-80':
        Ann = 2
    elif Ann == '60-70':
        Ann = 3
    elif Ann == 'Select':
        st.write('Select Percentage Again')
    return Ann

def In_normal(In):
    if In == 'Above 6L':
        In = 3
    elif In == '3L to 6L':
        In = 2
    elif In == '1.5L to 3L':
        In = 1
    elif In == 'Upto 1.5L':
        In = 0
    elif In == 'Select':
        st.write('Select Income Again')
    return In

def normal(edu,Gen,Ex,Dis,Ann,In,India):
    return clf(edu_normal(edu),Gen_normal(Gen),Ex_normal(Ex),Dis_normal(Dis),Ann_normal(Ann),In_normal(In),na_normal(India))

    

st.header("Scholarship Grant for Student" )


edu = st.selectbox(':green[Enter The Education Qualification of Student]',('Select','UG','PG','Dr.'))
Gen = st.selectbox(':green[Gender]',('Select','Male','Female'))
Ex = st.selectbox(':green[Is Your family has An Ex-service personal]',('Select','Yes','No'))
Dis = st.selectbox(':green[Do you have special needs]',('Select','Yes','No',))
Ann = st.selectbox(':green[What was your pass percentage]',('Select','90-100','80-90','70-80','60-70'))
In = st.selectbox(":green[What is your family' annual income]",('Select','Above 6L','3L to 6L','1.5L to 3L','Upto 1.5L'))
India = st.selectbox(":green[Resident of India?]",('Select','Yes','No'))

if st.button('Check'):
    if normal(edu,Gen,Ex,Dis,Ann,In,India) == 1:
        st.success("Granted!")
    else:
        st.error("Not Granted")
    # st.write("option selected",option)

ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left:300px;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align:left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/AbhishekRdev" target="_blank"> by Abhishek</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)