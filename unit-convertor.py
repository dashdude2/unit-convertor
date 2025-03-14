import streamlit as st 
st.markdown(
    """
    <style>
    body {
    background-color: #lele2f
    color: white
 }
.stApp{
    background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
    padding:38px;
    border-radius: 15px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
}
h1{
    text-align: center;
     font-size:36px;
    color: white;
 }
.stbutton>button{
    background: liner-gradient(45deg, #0b5394, #351c75);
    color: white;
    font-size: 18px;
    paddingL: 10px 20px;
    border-radius: 10px;
    transition: 0.3s;
    box-shadow: 0px 5px 15px  rgba(0, 281, 255,0.4);

 }
 .stbutton>button:hover{
    transform: scale(1.05);
    background: linear-gradient(45deg #92fe9d, #00c9ff);
    color: black;
 }
 .result-box {
 font-size: 25px;
 font-weight: italic;
 text-align: center; 
 background: rgba(255,255,255,0.05)
 padding: 15px;
 border-radius: 10px;
 margin-top: 20px;
 box-shadow: 0px 5px 15px rgba(0,201, 255,0.2);
 }
 .footer{
    text-align: center;
    margin-top: 40px;
    font-size: 14px;
    color: black;
 }
 </style> 
"""
)
unsafe_allow_html=True
#title and description:
st.markdown("<h1> unit convertor using python and streamlit</h1>",unsafe_allow_html=True)
st.write("easily convert between different units of length, weight and Temperature.")

#siderbar menu
conversion_type = st.sidebar.selectbox("choose conversion type",["length","weight","Temperature"])
value = st.number_input("enter value",value=0.0, min_value=0.0,step=0.1)
col1,col2 = st.columns(2)

if conversion_type == "length":
   with col1:
      from_unit = st.selectbox("from",["meter","kilometer","centimeter","millimeter","mile","yard","feet","inch"])
   with col2:
      to_unit = st.selectbox("to",["meter","kilometer","centimeter","millimeter","mile","yard","feet","inch"])
elif conversion_type == "weight":
   with col1:
      from_unit = st.selectbox("from",["kilogram","gram","milligram","pound","ounce"])
   with col2:
      to_unit = st.selectbox("to",["kilogram","gram","milligram","pound","ounce"])
elif conversion_type == "Temperature":
   with col1:
      from_unit = st.selectbox("from",["celsius","fahrenheit","kelvin"])
   with col2:
      to_unit = st.selectbox("to",["celsius","fahrenheit","kelvin"])
   
#converted function
def length_convertor(value,from_unit,to_unit):
   length_unit ={
      "meter":1,
      "kilometer":0.001,
      "centimeter":100,
      "millimeter":1000,
      "mile":0.000621371,
      "yard":1.09361,
      "feet":3.28,
      "inch":39.37
   }
   return(value / length_unit[from_unit] * length_unit[to_unit])

def weight_convertor(value,from_unit,to_unit):
   weight_unit ={
      "kilogram":1,
      "gram":1000,
      "milligram":1000000,
      "pound":2.20462,
      "ounce":35.27
   }
   return(value / weight_unit[from_unit] * weight_unit[to_unit])

   def temp_convertor(value, from_unit, to_unit):
      if from_unit == "celsius":
         return(value * 9/5 + 32) if to_unit == "fahrenheit" else (value + 273.15) if to_unit == "kelvin"else value
      elif from_unit == "fahrenheit":
         return((value - 32) * 5/9) if to_unit == "celsius" else (value - 459.67) if to_unit == "kelvin"else value
      elif from_unit =="kelvin":
         return(value - 273.15) if to_unit == "celsius" else(value -273.15) * 9/5 + 32 if to_unit == "fahrenheit"else value
         return value


#button for conversion
if st.button("🤖convert"):
   if conversion_type == "length":
      result = length_convertor(value, from_unit, to_unit)
   elif conversion_type == "weight":
      result = weight_convertor(value, from_unit, to_unit)
   elif conversion_type == "temprature":
      result = temp_convertor(value, from_unit, to_unit)

   st.markdown(f"<div class ='result-box'>{value} {from_unit} = {result:.4f} {to_unit}<div>", unsafe_allow_html=True)

st.markdown(f"div class =footer>developed by bunny </div>", unsafe_allow_html=True)



