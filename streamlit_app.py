import streamlit as st
import os

#page layout center
# set the page title and icon
st.set_page_config(page_title="Canary Tech", page_icon="	:factory:", layout="centered")

#construct the path of the img folder
img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'ressources/img'))



#center the title
st.markdown("""<h1 style="font-family: Garamond; 
text-align: center;">Canary Tech</h1>""", unsafe_allow_html=True)

#make 2 columns
col1, col2 = st.columns(2)

#in col1 the image
canary_path = os.path.join(img_path, 'canary_solo_200.png')
col1.image(canary_path, output_format = "PNG")
#create a title and sub-title for the app

#in col2 put some text
col2.markdown("""<br>""", unsafe_allow_html=True)
col2.markdown("""
#### After years of working in the industrial data engeering field, 
Otahy has developped Canary Tech. This concrete portofolio that will solve 3 existing pain points of your business in a digital world. """)

st.markdown("""We encounter 3 major pain points every time we are with industrial cusotmers:
* 1: Despite all my efforts I have critical orhpans data at the intersection of my ERP and other platforms, creating a major risks (quality, finance, compliance, ESG, etc...)
* 2: Everytime I run an analytic project to solve production issues, I start by cleaning, indexing, organising my time series data from machines with a huge associated cost.
* 3: I see more and more generative AI used by my emplpyees officially or not, how I can train my organisation?""")

#orphan data
st.markdown("""## Orphan Data :""")
st.markdown("""they exist becasue they are small, critical, coming from various sources at different frequencies:""")
st.markdown("""
* Lawers checking suppliers contracts and complicance then passing instructions to someone else to upload in SAP... 
could be scary if you block or enable the wrong subsidiary in a group.
* Chief engineer reviewed the product structure and validate the new BOM, but the new BOM is not uploaded in the PDM system.
* Fianance receiving recurring late request to validate project margin on Excel but with a questionable hourly rate.... 
no worries it is just a multi millions call for tender. """)

st.markdown("""We have developped a methodology to collect, index, organise, manipulate and secure your orphan process and data in a single place.  """)

st.markdown(""":sparkles: We inject the right amount of subject matter expert and IT skills, resuts are :""")
st.markdown("""* Your processes are captured with the right business rules and experts save times
* IT is finally "taping into" it as they face now a data model with clear rules""")

st.image(os.path.join(img_path, 'orphan_data.png'),output_format = "PNG")


#Times series indexer
st.markdown("""## Timeseries indexer :""")
st.markdown("""Back in a day, you walked into a library and you find 1000 books on the same topic, did you open each one and read it or
did you hope to find a book indexer with keywords, synthesis and sample pointing you to the right books?  
Same for the Web, you thank google for indexing websites continously.  
Why do you not have the same for your time series data from your machines?  """)


st.markdown("""Existing technologies allow to go through PetaByte of data and start indexing etc but at which cost? Here golden rules we learned working with cloud and timesries :   
* It's not because it is possible that it is the right thing to do
* Cloud providers don't crash they charge you
* Don't use serverless architecture when you can plan the workload
* Having IoT monitoring does not mean you data are "ready" for analytics""")

st.markdown("""Thanks to our work with industrial customers on non quality, data integration or predictive maintenance.  
:sparkles: We developped a pre processing methodoly to be applied continously on your machine data output, results are:  
* Reduce processing cost of accessing your data
* Reduce storage cost applying custom compression
* Increase data quality by continous cleaning
* Expose critical values, trend, outliners, etc... to your system engineers
* Enable data correlation accross your entire process to support production maturity""")

st.image(os.path.join(img_path, 'sensor_indexer_600.png'),output_format = "PNG")


#Times series indexer
st.markdown("""## Preventive AI Training :""")

st.markdown("""Starting in JAN 2024 ... Stay Tuned  
Today, organisation need to learn how to use generative AI and LLM model. Dedicated training will be providing for : """)

col1, col2 = st.columns(2)

col1.markdown(""" 
* Everybody: How interrogate safely a generative AI and validate the output
* Manager: How manage the skills recongising the added value of generative AI
* Executive: How to make decision with AI, understand coceptually LLM, training dataset and avoid bias""")


col2.image(os.path.join(img_path, 'preventive_ai _400.png'),output_format = "PNG")

st.markdown("""### Contact us for a demo or a POC:  
* [canarytech@otahy.com](mailto:canaryfab@otahy.com)
* [carvals@otahy.com](mailto:carvals@otahy.com)""")

#add orphan data image
#st.image(os.path.join(img_path, 'orphan_data.png'),output_format = "PNG")






