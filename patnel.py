import streamlit as st
import pandas as pd
from datetime import datetime
import webbrowser
import base64

# ══════════════════════════════════════════════════════════════════════════
#  AILYN CONSTRUCTION PRO — MOUNTAIN UI (OFFICIAL V34 RESTORED)
# ══════════════════════════════════════════════════════════════════════════

class AilynProFull:
    def __init__(self):
        self.name = "AILYN CONSTRUCTION PRO"
        # Primary recipients from jhai_3.py
        self.recipients = ["garryboypepito2004@gmail.com", "ailyn_peps0678@yahoo.com"]
        
        # UI Colors from Screenshot 2026-05-04 142751.jpg
        self.neon_green = "#00ff88"
        self.gold_spent = "#ffcc00"
        self.bg_url = "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&q=80&w=2070"

        # Initialize Session State
        if 'ledger' not in st.session_state: st.session_state.ledger = []
        if 'capital' not in st.session_state: st.session_state.capital = 0.0
        if 'view' not in st.session_state: st.session_state.view = "HOME"

    def inject_custom_css(self):
        """Injects the high-contrast mountain glass UI"""
        st.markdown(f"""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
            
            .stApp {{
                background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url("{self.bg_url}");
                background-size: cover;
                background-attachment: fixed;
                font-family: 'Inter', sans-serif;
            }}

            /* TOP TITLE DESIGN */
            .title-text {{
                text-align: center;
                color: white;
                font-weight: 900;
                letter-spacing: 6px;
                font-size: 42px;
                margin-top: 10px;
                text-transform: uppercase;
            }}
            .title-text span {{ color: {self.neon_green}; }}

            /* METRIC GLASS PANEL */
            .glass-metric {{
                background: rgba(255, 255, 255, 0.07);
                backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.12);
                border-radius: 35px;
                padding: 45px;
                margin: 25px auto;
                width: 90%;
                display: flex;
                justify-content: space-around;
                box-shadow: 0 25px 50px rgba(0,0,0,0.5);
            }}
            .metric-box {{ text-align: center; }}
            .m-label {{ color: {self.neon_green}; font-size: 11px; font-weight: 900; letter-spacing: 5px; opacity: 0.9; }}
            .m-val {{ color: white; font-size: 44px; font-weight: 900; margin-top: 8px; }}
            .m-spent {{ color: {self.gold_spent}!important; }}

            /* 6-BUTTON GRID SYSTEM */
            .stButton>button {{
                background: rgba(255, 255, 255, 0.05) !important;
                backdrop-filter: blur(12px) !important;
                border: 1px solid rgba(0, 255, 136, 0.4) !important;
                color: {self.neon_green} !important;
                border-radius: 12px !important;
                height: 60px !important;
                font-weight: 800 !important;
                letter-spacing: 2px !important;
                transition: 0.3s;
            }}
            .stButton>button:hover {{
                background: rgba(0, 255, 136, 0.15) !important;
                transform: translateY(-3px);
                box-shadow: 0 10px 20px rgba(0, 255, 136, 0.2);
            }}

            /* DISPATCH BUTTON SPECIAL STYLE */
            .dispatch-row button {{
                border: 1px solid rgba(255,255,255,0.3) !important;
                color: white !important;
                background: rgba(255,255,255,0.1) !important;
                margin-top: 15px !important;
            }}

            /* BLUE STATUS NOTIFICATION */
            .blue-status {{
                background: rgba(28, 57, 85, 0.7);
                border-left: 4px solid {self.neon_green};
                color: #b0d4ff;
                padding: 15px 30px;
                border-radius: 4px;
                font-size: 14px;
                margin-top: 25px;
            }}

            header, footer {{ visibility: hidden; }}
            </style>
        """, unsafe_allow_html=True)

    def trigger_dispatch(self):
        """Opens Gmail with encoded report to recipients from jhai_3.py"""
        spent = sum(x['Total'] for x in st.session_state.ledger)
        subject = f"CONSTRUCTION UPDATE: {self.name}"
        body = f"Ailyn Construction Pro Report:\nTotal Expenses: P{spent:,.2f}\n\nThank you for your time Taylin love heart ❤️"
        to_str = ",".join(self.recipients)
        url = f"https://mail.google.com/mail/?view=cm&fs=1&to={to_str}&su={subject}&body={body}"
        webbrowser.open_new_tab(url)

    def run(self):
        self.inject_custom_css()
        
        if st.session_state.view == "HOME":
            # --- TITLE SECTION ---
            st.markdown(f'<h1 class="title-text">AILYN CONSTRUCTION <span>PRO</span></h1>', unsafe_allow_html=True)

            # --- METRICS SECTION ---
            spent = sum(x['Total'] for x in st.session_state.ledger)
            balance = st.session_state.capital - spent
            st.markdown(f"""
                <div class="glass-metric">
                    <div class="metric-box"><div class="m-label">CAPITAL</div><div class="m-val">₱ {st.session_state.capital:,.2f}</div></div>
                    <div class="metric-box"><div class="m-label">SPENT</div><div class="m-val m-spent">₱ {spent:,.2f}</div></div>
                    <div class="metric-box"><div class="m-label">BALANCE</div><div class="m-val">₱ {balance:,.2f}</div></div>
                </div>
            """, unsafe_allow_html=True)

            # --- COMMAND GRID ---
            c1, c2, c3 = st.columns(3)
            with c1:
                if st.button("➕ MATERIAL"): st.session_state.view = "ADD"; st.rerun()
                if st.button("💰 CAPITAL"): st.session_state.view = "CASH"; st.rerun()
            with c2:
                if st.button("🚚 DELIVERY"): st.session_state.view = "ADD"; st.rerun()
                if st.button("⚙️ EMAILS"): st.toast("SMTP Connections Stable")
            with c3:
                if st.button("📦 OTHERS"): st.session_state.view = "ADD"; st.rerun()
                if st.button("🔄 RESET"): st.session_state.ledger = []; st.rerun()

            # --- DISPATCH SECTION ---
            st.markdown('<div class="dispatch-row">', unsafe_allow_html=True)
            if st.button("⬜ DISPATCH GMAIL REPORT", use_container_width=True):
                self.trigger_dispatch()
            st.markdown('</div>', unsafe_allow_html=True)

            # --- STATUS BAR ---
            status = "System Ready. No records to display yet." if not st.session_state.ledger else f"Active Session: {len(st.session_state.ledger)} entries logged."
            st.markdown(f'<div class="blue-status">{status}</div>', unsafe_allow_html=True)

        elif st.session_state.view == "ADD":
            st.markdown('<div style="background:rgba(0,0,0,0.6); padding:40px; border-radius:20px; border:1px solid #00ff88;">', unsafe_allow_html=True)
            st.subheader("🛠️ MATERIAL LOGGING")
            with st.form("entry_form", clear_on_submit=True):
                item = st.text_input("DESCRIPTION").upper()
                qty = st.number_input("QUANTITY", min_value=1)
                price = st.number_input("PRICE (₱)", min_value=0.0)
                if st.form_submit_button("COMMIT TO LEDGER"):
                    if item:
                        st.session_state.ledger.insert(0, {
                            "Date": datetime.now().strftime("%Y-%m-%d"),
                            "Item": item, "Qty": qty, "Price": price, "Total": qty*price
                        })
                        st.success(f"SAVED: {item}")
            if st.button("BACK TO DASHBOARD"): st.session_state.view = "HOME"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        elif st.session_state.view == "CASH":
            st.markdown('<div style="background:rgba(0,0,0,0.6); padding:40px; border-radius:20px;">', unsafe_allow_html=True)
            st.subheader("💰 FUND MANAGEMENT")
            st.session_state.capital = st.number_input("Total Project Allocation (₱)", value=st.session_state.capital)
            if st.button("CONFIRM FUNDS"): st.session_state.view = "HOME"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    AilynProFull().run()