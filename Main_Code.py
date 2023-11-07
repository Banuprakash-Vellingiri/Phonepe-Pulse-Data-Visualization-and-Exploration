# Importing neccessary libraries
import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image
import mysql.connector as mysql
#--------------------------------------------------------------------------------------------------------------------------------------------
#Connecting with MYSQL

mydb = mysql.connect(host="localhost",
                     user="root",
                     password="banu",
                     database="phonepe",
                     use_pure=True
                   )
mycursor = mydb.cursor(buffered=True)
#--------------------------------------------------------------------------------------------------------------------------------------------
# Setting up page configuration

st.set_page_config(page_title= "Phonepe Pulse Data Visualization by Banuprakash V",
                   layout= "wide",
                   page_icon="phonepegraph.png",
                   initial_sidebar_state= "expanded")
#--------------------------------------------------------------------------------------------------------------------------------------------
# Creating option menu in the side bar
st.sidebar.image("phonepegraph.png", caption=None, width=140, use_column_width=None, clamp=True, channels="RGB", output_format="auto")
with st.sidebar:
    selected = option_menu("Menu", ["Home","Top Charts","Explore Data"], 
                                    icons=["house-fill","rocket-takeoff-fill","bar-chart-line-fill"],
                                    menu_icon= "grid-fill",
                                    default_index=0,
                                    styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#6F99AD"},
                                            "nav-link-selected": {"background-color": "#6F36AD"}})
    
#--------------------------------------------------------------------------------------------------------------------------------------------
# HOME

if selected == "Home":
            st.info("# :white[Phonepe Pulse Data Visualization and Exploration]")
            st.markdown("## :blue[&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; A User-Friendly Tool Using Streamlit and Plotly]")
            col1,col2 = st.columns(2,gap="medium")
            col1.markdown("### :orange[Technologies Used :]")
            col1.markdown("### :white[ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;1.&nbsp;Python]")
            col1.markdown("### :white[ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;2.&nbsp;Github-Cloning]")
            col1.markdown("### :white[ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;3.&nbsp;Streamlit]")
            col1.markdown("### :white[ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;4.&nbsp;MySQL]")
            col1.markdown("### :white[ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;4.&nbsp;Plotly]")
            col1.markdown("### :orange[Synopsis:]")
            col1.markdown("### :white[:blue[Step 1]: Extract data from the Phonepe pulse Github repository through python scripting and cloning the data.]")
            col1.markdown("### :white[:blue[Step 2]: Cloned data is converted into pandas Data frame and required cleaning operations are carried out. ]")
            col1.markdown("### :white[:blue[Step 3]: After cleaning,the data transferred into a MySQL database for storing and for efficient retrieval.]")
            col1.markdown("### :white[:blue[Step 4]: Using streamlit,the data visualisation dashboard is builded.]")
            col1.markdown("### :white[:blue[Step 5]: Valuable insights are gained by querying the data and visualised in dashboard using Plotly.]")
            col2.write("##  ")
            col2.write("##  ")
            col2.write("##  ")
            col2.image("phonepelogo.png")

#--------------------------------------------------------------------------------------------------------------------------------------------
#TOP CHARTS

if selected == "Top Charts":
            
            #Side_bar - select_box
            select = st.sidebar.selectbox(" :white[**Category :**]", ("Transactions", "Users"))
            #------------------------------------------------------------------------------------
            st.info("## :white[Top Charts]")
            Year = st.slider("**Year**", min_value=2018, max_value=2023)
            Quarter = st.slider("**Quarter**", min_value=1, max_value=4)
            st.markdown(f"## Data of &nbsp; Year &nbsp;  -  :orange[{Year}] &nbsp;(Quarter - :orange[{Quarter}]) &nbsp; :")
            st.write("# ")
            #---------------------------------------------------------------------------------------------------------------------------
            # Top Charts>>>Side_bar>>>Transactions

            if select== "Transactions":
                       col1,col2=st.columns(2,gap="small")
                       col3,col4= st.columns(2,gap="small")
                       if Year==2023 and Quarter==4:
                              st.markdown("## :red[#Sorry No Data to Display!!!]")
                       else:
                            with col1:
                                st.markdown("### :violet[State]")
                                mycursor.execute(f"select state, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total from agg_trans where year = {Year} and quarter = {Quarter} group by state order by Total desc limit 10")
                                df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Transactions_Count','Total_Amount'])
                                fig = px.pie(df, values='Total_Amount',
                                                 names='State',
                                                 title='Top 10',
                                                 color_discrete_sequence=px.colors.sequential.Agsunset,
                                            ) 

                                fig.update_traces(textposition='inside', textinfo='percent+label')
                                st.plotly_chart(fig,use_container_width=True)
                                
                            with col2:
                                st.markdown("### :violet[District]")
                                mycursor.execute(f"select district , sum(Count) as Total_Count, sum(Amount) as Total from map_trans where year = {Year} and quarter = {Quarter} group by district order by Total desc limit 10")
                                df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Transactions_Count','Total_Amount'])

                                fig = px.pie(df, values='Total_Amount',
                                                names='District',
                                                title='Top 10',
                                                color_discrete_sequence=px.colors.sequential.Agsunset,
                                            )

                                fig.update_traces(textposition='inside', textinfo='percent+label')
                                st.plotly_chart(fig,use_container_width=True)
                                
                            with col3:
                                st.markdown("### :violet[Pincode]")
                                mycursor.execute(f"select pincode, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total from top_trans where year = {Year} and quarter = {Quarter} group by pincode order by Total desc limit 10")
                                df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Transactions_Count','Total_Amount'])
                                fig = px.pie(df, values='Total_Amount',
                                                names='Pincode',
                                                title='Top 10',
                                                color_discrete_sequence=px.colors.sequential.Agsunset,
                                            )

                                fig.update_traces(textposition='inside', textinfo='percent+label')
                                st.plotly_chart(fig,use_container_width=True)
            #---------------------------------------------------------------------------------------------------------------------------              
            # Top Charts>>>Select_box>>Users    
                  
            if select== "Users":
                        col1,col2=st.columns(2,gap="small") 
                        col3,col4=st.columns(2,gap="small")    
                        with col1:
                            st.markdown("### :violet[Brands]")
                            if Year == 2022 and Quarter in [2,3,4]:
                                st.markdown("## :red[#Sorry No Data to Display!!!]")
                            elif Year==2023 and Quarter in [1,2,3,4]:
                                st.markdown("## :red[#Sorry No Data to Display!!!]")
                            else:
                                mycursor.execute(f"select brands, sum(count) as Total_Count, avg(percentage)*100 as Avg_Percentage from agg_user where year = {Year} and quarter = {Quarter} group by brands order by Total_Count limit 10")
                                df = pd.DataFrame(mycursor.fetchall(), columns=['Brand', 'Total_Users','Avg_Percentage'])
                                fig = px.pie(df,
                                                values='Total_Users',
                                                names='Brand',
                                                title='Top 10',
                                                color_discrete_sequence=px.colors.sequential.Agsunset,
                                                hover_data=['Total_Users']
                                            )
                                fig.update_traces(textposition='inside', textinfo='percent+label')
           
                                st.plotly_chart(fig,use_container_width=True)   
                    
                        with col2:
                            st.markdown("### :violet[District]")
                            mycursor.execute(f"select district, sum(Registered_User) as Total_Users, sum(app_opens) as Total_Appopens from map_user where year = {Year} and quarter = {Quarter} group by district order by Total_Users limit 10")
                            df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Total_Users','Total_Appopens'])
                            df.Total_Users = df.Total_Users.astype(float)
                            fig = px.pie(df,
                                                values='Total_Users',
                                                names='District',
                                                title='Top 10',
                                                color_discrete_sequence=px.colors.sequential.Agsunset,
                                                hover_data=['Total_Users']
                                            )
                            fig.update_traces(textposition='inside', textinfo='percent+label')
                 
                            st.plotly_chart(fig,use_container_width=True)
                            
                        with col3:
                            st.markdown("### :violet[Pincode]")
                            mycursor.execute(f"select Pincode, sum(Registered_Users) as Total_Users from top_user where year = {Year} and quarter = {Quarter} group by Pincode order by Total_Users desc limit 10")
                            df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Total_Users'])
                            fig = px.pie(df,
                                            values='Total_Users',
                                            names='Pincode',
                                            title='Top 10',
                                            color_discrete_sequence=px.colors.sequential.Agsunset,
                                            hover_data=['Total_Users']
                                        )
                            fig.update_traces(textposition='inside', textinfo='percent+label')
                            st.plotly_chart(fig,use_container_width=True)
                            
                        with col4:
                            st.markdown("### :violet[State]")
                            mycursor.execute(f"select state, sum(Registered_user) as Total_Users, sum(App_opens) as Total_Appopens from map_user where year = {Year} and quarter = {Quarter} group by state order by Total_Users desc limit 10")
                            df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Users','Total_Appopens'])
                            fig = px.pie(df, values='Total_Users',
                                            names='State',
                                            title='Top 10',
                                            color_discrete_sequence=px.colors.sequential.Agsunset,
                                            hover_data=['Total_Appopens'],
                                            labels={'Total_Appopens':'Total_Appopens'})

                            fig.update_traces(textposition='inside', textinfo='percent+label')
                            st.plotly_chart(fig,use_container_width=True)
#--------------------------------------------------------------------------------------------------------------------------------------------
# EXPLORE DATA

if selected == "Explore Data":
            
            #Side_bar - select_box
            select = st.sidebar.selectbox("**Type**", ("Transactions", "Users"))
            #----------------------------------------------------------------------------------------------------
            st.info("## :white[Explore Data]")
            Year = st.slider("**Year**", min_value=2018, max_value=2023)
            Quarter = st.slider("**Quarter**", min_value=1, max_value=4)
            st.markdown(f"## Data of &nbsp; Year &nbsp;  -  :orange[{Year}] &nbsp;(Quarter - :orange[{Quarter}]) &nbsp; :")
            st.write("# ")
            #----------------------------------------------------------------------------------------------------

            # Explore Data>>>Side_bar>>>Transactions
            if select  == "Transactions":
                  if Year==2023 and Quarter ==4:
                        st.markdown("## :red[#Sorry No Data to Display!!!]")
                  else: 
                        col1,col2 = st.columns(2) 

                        with col1:
                            st.markdown("## :violet[Overall State Data - Transactions Amount]")
                            mycursor.execute(f"select state, sum(count) as Total_Transactions, sum(amount) as Total_amount from map_trans where year = {Year} and quarter = {Quarter} group by state order by state")
                            df1 = pd.DataFrame(mycursor.fetchall(),columns= ['State', 'Total_Transactions', 'Total_amount'])
                            df1.Total_amount = df1.Total_amount.astype(float)
                            df2 = pd.read_csv('Statenames.csv')
                            df1.State = df2

                            fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                                    featureidkey='properties.ST_NM',
                                                    locations='State',
                                                    color='Total_amount',
                                                    color_continuous_scale='sunset',
                                                    labels={'Total_amount': 'Total Amount'}
                                               )

                            fig.update_geos(fitbounds="locations", visible=False)
                            st.plotly_chart(fig,use_container_width=True)
                        #----------------------------------------------------------------------------------------------------
                        with col2:                            
                            st.markdown("## :violet[Overall State Data - Transactions Count]")
                            mycursor.execute(f"select state, sum(count) as Total_Transactions, sum(amount) as Total_amount from map_trans where year = {Year} and quarter = {Quarter} group by state order by state")
                            df1 = pd.DataFrame(mycursor.fetchall(),columns= ['State', 'Total_Transactions', 'Total_amount'])
                            df2 = pd.read_csv('Statenames.csv')
                            # df1.Total_Transactions = df1.Total_Transactions.astype(np.int64)
                            df1.Total_Transactions = df1.Total_Transactions.astype(float)
                            df1.State = df2

                            fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                                    featureidkey='properties.ST_NM',
                                                    locations='State',
                                                    color='Total_Transactions',
                                                    color_continuous_scale='sunset',
                                                    labels={'Total_amount': 'Total Amount'}
                                                )

                            fig.update_geos(fitbounds="locations", visible=False)
                            st.plotly_chart(fig,use_container_width=True)
                        #----------------------------------------------------------------------------------------------------    
                        # BAR CHART - TOP PAYMENT TYPE
                        st.markdown("## :violet[Top Payment Type :]")
                        mycursor.execute(f"select Transaction_type, sum(Transaction_count) as Total_Transactions, sum(Transaction_amount) as Total_amount from agg_trans where year= {Year} and quarter = {Quarter} group by transaction_type order by Transaction_type")
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Transaction_type', 'Total_Transactions','Total_amount'])

                        fig = px.bar(df,
                                        title='Transaction Types vs Total_Transactions',
                                        x="Transaction_type",
                                        y="Total_Transactions",
                                        orientation='v',
                                        color='Total_amount',
                                        color_continuous_scale=px.colors.sequential.Agsunset
                                    )
                        st.plotly_chart(fig,use_container_width=False)
                        #----------------------------------------------------------------------------------------------------  
                        # BAR CHART TRANSACTIONS - DISTRICT WISE DATA            
                        st.markdown("# ")
                        st.markdown("# ")
                        st.markdown("# ")
                        st.markdown("## :violet[Select State:]")
                        selected_state = st.selectbox("",
                                            ('andaman-&-nicobar-islands','andhra-pradesh','arunachal-pradesh','assam','bihar',
                                            'chandigarh','chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana',
                                            'himachal-pradesh','jammu-&-kashmir','jharkhand','karnataka','kerala','ladakh','lakshadweep',
                                            'madhya-pradesh','maharashtra','manipur','meghalaya','mizoram',
                                            'nagaland','odisha','puducherry','punjab','rajasthan','sikkim',
                                            'tamil-nadu','telangana','tripura','uttar-pradesh','uttarakhand','west-bengal'),index=30)
                        st.markdown(f"## District wise transactions of :orange[{selected_state.title()}]:")

                        mycursor.execute(f"select State, District,year,quarter, sum(count) as Total_Transactions, sum(amount) as Total_amount from map_trans where year = {Year} and quarter = {Quarter} and State = '{selected_state}' group by State, District,year,quarter order by state,district")
                        
                        df1 = pd.DataFrame(mycursor.fetchall(), columns=['State','District','Year','Quarter',
                                                                        'Total_Transactions','Total_amount'])
                        fig = px.bar(df1,
                                        title=selected_state,
                                        x="District",
                                        y="Total_Transactions",
                                        orientation='v',
                                        color='Total_amount',
                                        color_continuous_scale=px.colors.sequential.Agsunset
                                    )
                        st.plotly_chart(fig,use_container_width=True)
        #----------------------------------------------------------------------------------------------------  

        #   Explore Data>>>Side_bar>>>Users          
            if select  == "Users": 
                  if Year==2023 and Quarter ==4:
                        st.markdown("## :red[#Sorry No Data to Display!!!]")
                  else:
                        # Overall State Data - TOTAL APPOPENS - INDIA MAP
                        st.markdown("## :violet[Overall State Data - User App opening frequency]")
                        mycursor.execute(f"select state, sum(Registered_user) as Total_Users, sum(App_opens) as Total_Appopens from map_user where year = {Year} and quarter = {Quarter} group by state order by state")
                        df1 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Users','Total_Appopens'])
                        df1.Total_Appopens = df1.Total_Appopens.astype(float)
                        df2 = pd.read_csv('Statenames.csv')
                        df1.State = df2
                        
                        fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                                featureidkey='properties.ST_NM',
                                                locations='State',
                                                color='Total_Appopens',
                                                color_continuous_scale='sunset',
                                                labels={'Total_Appopens': 'Total App Opens'}
                                           )

                        fig.update_geos(fitbounds="locations", visible=False)
                        st.plotly_chart(fig,use_container_width=True)
                        
                        # BAR CHART TOTAL UERS - DISTRICT WISE DATA 
                        st.markdown("## :violet[Select State :]")
                        selected_state = st.selectbox("",
                                            ('andaman-&-nicobar-islands','andhra-pradesh','arunachal-pradesh','assam','bihar',
                                            'chandigarh','chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana',
                                            'himachal-pradesh','jammu-&-kashmir','jharkhand','karnataka','kerala','ladakh','lakshadweep',
                                            'madhya-pradesh','maharashtra','manipur','meghalaya','mizoram',
                                            'nagaland','odisha','puducherry','punjab','rajasthan','sikkim',
                                            'tamil-nadu','telangana','tripura','uttar-pradesh','uttarakhand','west-bengal'),index=30)
                        st.markdown(f"## District wise users of :orange[{selected_state.title()}]:")

                        mycursor.execute(f"select State,year,quarter,District,sum(Registered_user) as Total_Users, sum(App_opens) as Total_Appopens from map_user where year = {Year} and quarter = {Quarter} and state = '{selected_state}' group by State, District,year,quarter order by state,district")
                        df = pd.DataFrame(mycursor.fetchall(), columns=['State','year', 'quarter', 'District', 'Total_Users','Total_Appopens'])
                        df.Total_Users = df.Total_Users.astype(int)
                        
                        fig = px.bar(df,
                                        title=selected_state,
                                        x="District",
                                        y="Total_Users",
                                        orientation='v',
                                        color='Total_Users',
                                        color_continuous_scale=px.colors.sequential.Agsunset
                                    )
                        st.plotly_chart(fig,use_container_width=True)
                        
