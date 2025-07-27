import streamlit as st
import pandas as pd
from interest_calc import interest_cal_function  # Import your custom function
from interest_calc import val_for_bulk_interest


st.set_page_config(page_title="Interest Calculator", layout="wide")

# Create 4 tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Inputs",
    "Interest Rate (Monthly)",
    "Interest Rate (Daily)",
    "Bulk_Interest_File",
    "About"
])

# Initialize session state to store results
if 'df_final' not in st.session_state:
    st.session_state.df_final = None
if 'df_final_monthly' not in st.session_state:
    st.session_state.df_final_monthly = None

# --- TAB 1: INPUTS ---
with tab1:
    st.header("Interest Calculation Inputs")

    # Invoice Amount
    val_principal = st.number_input("Invoice Amount", format="%.4f")

    # Start and End Dates
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")

    # Payment Inputs
    st.subheader("Payments Received")
    num_payments = st.number_input("Number of Payments", min_value=0, step=1, value=0)

    lst_payment_amount = []
    lst_payment_date = []
    
    if num_payments > 0:
        for i in range(num_payments):
            col1, col2 = st.columns(2)
            with col1:
                amt = st.number_input(f"Payment {i+1} Amount", format="%.4f", key=f"amt_{i}")
                lst_payment_amount.append(amt)
            with col2:
                date = st.date_input(f"Payment {i+1} Date", key=f"date_{i}")
                lst_payment_date.append(date)

    import os
    
    # Upload Interest Rate Table CSV
    st.subheader("Upload Interest Rate Table")
    interest_file = st.file_uploader("Upload CSV", type=["csv"])
    default_path = "interest_rate_table.csv"
    
    # Option to use default file
    use_default = st.checkbox("Use default interest rate file", value=False)
    
    
    # Read file logic
    if interest_file is not None:
        df_interest_rate_month = pd.read_csv(interest_file)
        st.success("Uploaded file loaded.")
    elif use_default:
        if os.path.exists(default_path):
            df_interest_rate_month = pd.read_csv(default_path)
            st.success(f"Default file loaded from: {default_path}")
        else:
            st.error(f"Default file not found at: {default_path}")
    else:
        st.warning("Please upload a file or check the box to use the default file.")

    # points Inputs
    st.subheader("Set Decimal points to")
    num_decimal_point = st.number_input("Decimal Points", min_value=0, step=1, value=2)

    if st.button("Calculate Interest"):
        try:
            df_interest_rate_month = pd.read_csv(interest_file)
        except:
            pass
        df_interest_rate_month['Month'] = pd.to_datetime(df_interest_rate_month['End of'], format='%b-%y').dt.strftime('%m-%Y')
        df_interest_rate_month['InterestRate'] = df_interest_rate_month["Interest Rate"]*100
 
        # Convert all dates to string format "dd-mm-yyyy"
        str_start_date = start_date.strftime("%d-%m-%Y")
        # # print(str_start_date)
        str_end_date = end_date.strftime("%d-%m-%Y")
        # # print(str_end_date)
        str_payment_dates = [d.strftime("%d-%m-%Y") for d in lst_payment_date]

        try:
            df_final, df_final_monthly = interest_cal_function(
                val_principal,
                str_start_date,
                str_end_date,
                str_payment_dates,
                lst_payment_amount,
                df_interest_rate_month,
                num_decimal_point
                
            )
            # # print(df_final)
            # # print(df_final_monthly)
            
            # Store in session state
            st.session_state.df_final = df_final
            st.session_state.df_final_monthly = df_final_monthly
            
            st.markdown(
                """
                <div style="
                    position:fixed;
                    top: 40%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    background-color: #303030;
                    padding: 20px 30px;
                    border: 2px solid #ff6675;
                    border-radius: 10px;
                    box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
                    z-index: 1000;
                ">
                    <h1 style="color:#ffa947; text-align:center;text-decoration: underline;">Interest Calculation Done!</h1>
                    <h5 style="color:#4CAF50; text-align:center;"> Interest Calcuated</h5>
                    <h3 style="color:#bdffb0; text-align:center;">✅ """+str(round(df_final_monthly.iloc[-1,8],num_decimal_point))+"""</h3>
                    <h5 style="color:#4CAF50; text-align:center;"> Total Amount Calculated</h5>
                    <h3 style="color:#bdffb0; text-align:center;">✅ """+str(round(df_final_monthly.iloc[-1,-1],num_decimal_point))+"""</h3>
                    <p style="text-align:center;">Check the Monthly and Daily tabs for detailed results.</p>
                </div>
                """, unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"Error in interest calculation: {e}")

# --- TAB 2: MONTHLY OUTPUT ---
with tab2:
    st.header("Interest Rate (Monthly)")
    if st.session_state.df_final_monthly is not None:
        st.dataframe(st.session_state.df_final_monthly)
    else:
        st.info("Please input data and calculate in Tab 1.")

# --- TAB 3: DAILY OUTPUT ---
with tab3:
    st.header("Interest Rate (Daily)")
    if st.session_state.df_final is not None:
        st.dataframe(st.session_state.df_final)
    else:
        st.info("Please input data and calculate in Tab 1.")



# --- TAB 4: Simple File Calc ---
from io import BytesIO
with tab4:
    st.header("📁 Bulk File Interest Calculation")
    # uploading bulk file
    st.subheader("Upload Bulk Interest Table Below")
    uploaded_file = st.file_uploader("Upload Input CSV file", type="csv", key="file_tab5")
    # uploading interest file
    
    # Upload Interest Rate Table CSV
    st.subheader("Upload Interest Rate Table")
    interest_file_bulk = st.file_uploader("Upload CSV", type=["csv"], key="file_tab5_2")

    # Read file logic
    if interest_file_bulk is not None:
        df_interest_rate_month = pd.read_csv(interest_file_bulk)
        st.success("Uploaded file loaded.")
    else:
        st.warning("Please upload a file or check the box to use the default file.")


    #if st.button("Calculate Interest For Bulk"):
      #  try:
        #    df_interest_rate_month = pd.read_csv(interest_file)
   #     except:
     #       pass
       # df_interest_rate_month['Month'] = pd.to_datetime(df_interest_rate_month['End of'], format='%b-%y').dt.strftime('%m-%Y')
      #  df_interest_rate_month['InterestRate'] = df_interest_rate_month["Interest Rate"]*100
 
    
    if uploaded_file:
        df_interest_rate_month['Month'] = pd.to_datetime(df_interest_rate_month['End of'], format='%b-%y').dt.strftime('%m-%Y')
        df_interest_rate_month['InterestRate'] = df_interest_rate_month["Interest Rate"]*100
 
        df_input = pd.read_csv(uploaded_file)
        st.dataframe(df_input.head())
        st.info("Showing first 5 observations as sample data uploaded.")

        if st.button("Submit and Download Result"):
            try:
                
                df_input = val_for_bulk_interest(df_input, df_interest_rate_month)
                # Convert to Excel/CSV in memory
                output = BytesIO()
                df_input.to_csv(output, index=False)
                output.seek(0)

                # Auto download
                st.download_button(
                    label="📥 Download Modified CSV",
                    data=output,
                    file_name="Modified_File.csv",
                    mime="text/csv"
                )

                st.success("✅ Operation successful. File ready to download below.")
                st.dataframe(df_input)

            except Exception as e:
                st.error(f"⚠️ Error processing file: {e}")
        else:
            st.info("Please Press Submit and Wait 2-3 mins.")     
# --- TAB 5: ABOUT ---
with tab5:
    st.header("Created By Reshma George")
    # st.markdown("""
    # ---This app calculates interest accumulation on unpaid invoices with received payments, using both daily and monthly compounding.
    # """, unsafe_allow_html=True)

    st.markdown("""
    <h6 style='margin-top:20px;'>
        <span style='font-size:18px; color:#d6336c;'>This Application designed to calculate Interest on Single Input for Monthly, Daily and Multiple Inputs for Bulk File Inputs</span>
    </h6>
    
    """, unsafe_allow_html=True)

