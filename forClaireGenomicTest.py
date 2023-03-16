import streamlit as st
import pandas as pd
import numpy as np
import re

st.set_page_config(layout="wide")


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file,encoding='unicode_escape',skiprows=17)
    st.write(dataframe)


df_test=pd.read_csv('example_23JU069CH0002.csv',encoding='utf-8')

vkorc1=pd.read_csv('VKORC1_output.csv',encoding='utf-8')
tpmt=pd.read_csv('TPMT_output.csv',encoding='utf-8')
slco1b1=pd.read_csv('SLCO1B1_output.csv',encoding='utf-8')
nudt15=pd.read_csv('NUDT15_output.csv',encoding='utf-8')
dpyd=pd.read_csv('DPYD_output.csv',encoding='utf-8')
cyp3a5=pd.read_csv('CYP3A5_output.csv',encoding='utf-8')
cyp2c19=pd.read_csv('CYP2C19_output.csv',encoding='utf-8')
cyp2b6=pd.read_csv('CYP2B6_output.csv',encoding='utf-8')
abcg2=pd.read_csv('ABCG2_output.csv',encoding='utf-8')

with st.expander("test table"):
    st.dataframe(df_test,width=1000,height=1000)



with st.expander("genes with alleles"):
    st.write('VKORC1')
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(vkorc1,width=1000)
    with col2:
        vkorc1_allele_row=st.selectbox('select vkorc1 row',vkorc1.index)
    st.write('TPMT')
    col1, col2 = st.columns(2)    
   
    with col1:
        st.dataframe(tpmt,width=1000)
    with col2:
        tpmt_allele_row=st.selectbox('select tpmt row',tpmt.index)
    st.write('SLCO1B1')
    col1, col2 = st.columns(2)    
    
    with col1:
        st.dataframe(slco1b1,width=1000)
    with col2:
        slco1b1_allele_row=st.selectbox('select slco1b1 row',slco1b1.index)
    st.write('NUDT15')
    col1, col2 = st.columns(2)
   
    with col1:        
        st.dataframe(nudt15,width=1000)
    with col2:
        nudt15_allele_row=st.selectbox('select nudt15 row',nudt15.index)
    st.write('DPYD')
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(dpyd,width=1000)
    with col2:
        dpyd_allele_row=st.selectbox('select dpyd row',dpyd.index)
    st.write('CYP3A5')
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(cyp3a5,width=1000)
    with col2:
        cyp3a5_allele_row=st.selectbox('select cyp3a5 row',cyp3a5.index)
    st.write('CYP2C19')
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(cyp2c19,width=1000)
    with col2:
        cyp2c19_allele_row=st.selectbox('select cyp2c19 row',cyp2c19.index)
    st.write('CYP2B6')
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(cyp2b6,width=1000)
    with col2:
        cyp2b6_allele_row=st.selectbox('select cyp2b6 row',cyp2b6.index)
   
    st.write('ABCG2')
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(abcg2,width=1000)
    with col2:
        abcg2_allele_row=st.selectbox('select abcg2 row',abcg2.index)




sample_substitute=st.selectbox('select sample',df_test['Sample ID'].drop_duplicates())

vkorc1_allele_selected=vkorc1.iloc[vkorc1_allele_row]
vkorc1_allele_selected=pd.DataFrame(vkorc1_allele_selected).reset_index()
vkorc1_allele_selected.columns=['NCBI SNP Reference','New_Call']
vkorc1_allele_selected['Sample ID']=sample_substitute


tpmt_allele_selected=tpmt.iloc[tpmt_allele_row]
tpmt_allele_selected=pd.DataFrame(tpmt_allele_selected).reset_index()
tpmt_allele_selected.columns=['NCBI SNP Reference','New_Call']
tpmt_allele_selected['Sample ID']=sample_substitute


slco1b1_allele_selected=slco1b1.iloc[slco1b1_allele_row]
slco1b1_allele_selected=pd.DataFrame(slco1b1_allele_selected).reset_index()
slco1b1_allele_selected.columns=['NCBI SNP Reference','New_Call']
slco1b1_allele_selected['Sample ID']=sample_substitute




nudt15_allele_selected=nudt15.iloc[nudt15_allele_row]
nudt15_allele_selected=pd.DataFrame(nudt15_allele_selected).reset_index()
nudt15_allele_selected.columns=['NCBI SNP Reference','New_Call']
nudt15_allele_selected['Sample ID']=sample_substitute


dpyd_allele_selected=dpyd.iloc[dpyd_allele_row]
dpyd_allele_selected=pd.DataFrame(dpyd_allele_selected).reset_index()
dpyd_allele_selected.columns=['NCBI SNP Reference','New_Call']
dpyd_allele_selected['Sample ID']=sample_substitute


cyp3a5_allele_selected=cyp3a5.iloc[cyp3a5_allele_row]
cyp3a5_allele_selected=pd.DataFrame(cyp3a5_allele_selected).reset_index()
cyp3a5_allele_selected.columns=['NCBI SNP Reference','New_Call']
cyp3a5_allele_selected['Sample ID']=sample_substitute


cyp2c19_allele_selected=cyp2c19.iloc[cyp2c19_allele_row]
cyp2c19_allele_selected=pd.DataFrame(cyp2c19_allele_selected).reset_index()
cyp2c19_allele_selected.columns=['NCBI SNP Reference','New_Call']
cyp2c19_allele_selected['Sample ID']=sample_substitute


cyp2b6_allele_selected=cyp2b6.iloc[cyp2b6_allele_row]
cyp2b6_allele_selected=pd.DataFrame(cyp2b6_allele_selected).reset_index()
cyp2b6_allele_selected.columns=['NCBI SNP Reference','New_Call']
cyp2b6_allele_selected['Sample ID']=sample_substitute


abcg2_allele_selected=abcg2.iloc[abcg2_allele_row]
abcg2_allele_selected=pd.DataFrame(abcg2_allele_selected).reset_index()
abcg2_allele_selected.columns=['NCBI SNP Reference','New_Call']
abcg2_allele_selected['Sample ID']=sample_substitute

every_allele=pd.concat((vkorc1_allele_selected,tpmt_allele_selected,slco1b1_allele_selected,nudt15_allele_selected,dpyd_allele_selected,cyp3a5_allele_selected,cyp2c19_allele_selected,cyp2b6_allele_selected,abcg2_allele_selected))

with st.expander('new alleles selected'):
    st.dataframe(every_allele,width=1000)

df_test_w_edit=pd.merge(df_test,every_allele,how='left',on=['Sample ID','NCBI SNP Reference'])

def see_if_new(x):

    if not pd.isna(x['New_Call']):
        return x['New_Call']
    else:
        return x['Call']


df_test_w_edit['Call']=df_test_w_edit.apply(lambda x: see_if_new(x),axis=1) 

df_test_w_edit.drop('New_Call',axis=1,inplace=True)

with st.expander('new table'):
    st.dataframe(df_test_w_edit,width=1000)


f = open('new_table.csv', 'w+')
f.write('# Exported By : GUEST\n')
f.write('# Export Date : 08/10/2022 11:25:05 EDT\n')
f.write('# Study Name : 1 sample plate\n')
f.write('# Experiment Type : Real-time\n')
f.write('# Instrument Type : QuantStudioô 12K Flex Real-Time PCR System\n')
f.write('# Software Version Number : 1.4.0\n')
f.write('# Creation Date : 08/10/2022 11:23:32 EDT\n')
f.write('# Created By : GUEST\n')
f.write('# Last Modified Date : 08/10/2022 11:25:04 EDT\n')
f.write('# Last Modified By : GUEST\n')
f.write('# Template File Name : N/A\n')
f.write('# Template Originating Study Name : N/A\n')
f.write('# Template Creation Date : N/A\n')
f.write('# Template Created By User ID : N/A\n')
f.write('# Template Software Version Number :  N/A\n')
f.write('\n')
f.write('\n')

df_test_w_edit.to_csv(f,index=False)

f.write('\n')

pd.read_csv('atbottom.csv').to_csv(f,index=False)


f.close()

with open("new_table.csv", "rb") as file:

    st.download_button('download the new table',file,file_name='new_table.csv')