import streamlit as st

# Set up the page
st.set_page_config(page_title="Math Buddy", page_icon="🧮")

# Initialize session state to store problems
if 'problems' not in st.session_state:
    st.session_state.problems = []
if 'show_result' not in st.session_state:
    st.session_state.show_result = False
if 'user_answer' not in st.session_state:
    st.session_state.user_answer = None

def check_answer(correct_ans, user_ans):
    """Check if the user's answer is correct"""
    try:
        if int(user_ans) == int(correct_ans):
            return True
        else:
            return False
    except:
        return False

def main():
    # Header
    st.title("🧮 FIRST FOUR Pre-School")
    st.header("Math Buddy")
    st.divider()
    
    # Instructions
    st.info("**Operations:** ➕ Addition  ➖ Subtraction  ✖️ Multiplication  ➗ Division")
    
    # Create two columns for layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Enter a New Problem")
        
        # Operator selection
        operator = st.selectbox(
            "Choose Operation:",
            ["➕ Addition (+)", "➖ Subtraction (-)", "✖️ Multiplication (×)", "➗ Division (÷)"]
        )
        
        # Input fields based on operator
        if "Addition" in operator:
            first_num = st.number_input("Enter Augend (first number):", value=0, step=1)
            second_num = st.number_input("Enter Addend (second number):", value=0, step=1)
            correct_answer = first_num + second_num
            op_symbol = "+"
            
        elif "Subtraction" in operator:
            first_num = st.number_input("Enter Minuend (first number):", value=0, step=1)
            second_num = st.number_input("Enter Subtrahend (second number):", value=0, step=1)
            correct_answer = first_num - second_num
            op_symbol = "-"
            
        elif "Multiplication" in operator:
            first_num = st.number_input("Enter Multiplier (first number):", value=0, step=1)
            second_num = st.number_input("Enter Multiplicand (second number):", value=0, step=1)
            correct_answer = first_num * second_num
            op_symbol = "×"
            
        else:  # Division
            first_num = st.number_input("Enter Dividend (first number):", value=0, step=1)
            second_num = st.number_input("Enter Divisor (second number):", value=1, step=1)
            
            if second_num == 0:
                st.error("⚠️ ERROR: You can't divide a number by zero!")
                correct_answer = None
            else:
                correct_answer = first_num / second_num
            op_symbol = "÷"
        
        # Answer input
        user_answer = st.number_input("Enter Your Answer:", value=0, step=1, key="answer_input")
        
        # Submit button
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("✅ Check Answer", use_container_width=True):
                if correct_answer is not None:
                    if check_answer(correct_answer, user_answer):
                        st.success("🎉 Correct Answer! Great job!")
                        # Add to problems list
                        st.session_state.problems.append({
                            'first': first_num,
                            'operator': op_symbol,
                            'second': second_num,
                            'answer': correct_answer
                        })
                    else:
                        st.error(f"❌ Incorrect answer! The correct answer is {correct_answer}")
        
        with col_btn2:
            if st.button("🗑️ Clear All Problems", use_container_width=True):
                st.session_state.problems = []
                st.rerun()
    
    with col2:
        st.subheader("Problem Summary")
        
        if st.session_state.problems:
            st.write(f"**Total Problems:** {len(st.session_state.problems)}")
            
            # Display problems in a nice format
            st.write("---")
            for idx, prob in enumerate(st.session_state.problems, 1):
                st.write(f"**Problem {idx}:**")
                st.code(f"{prob['first']:>5}\n{prob['operator']}{prob['second']:>4}\n-----\n{prob['answer']:>5}")
        else:
            st.write("No problems yet! Start solving above. 👆")
    
    # Show all problems in table format at the bottom
    if st.session_state.problems:
        st.divider()
        st.subheader("All Your Work:")
        
        # Create formatted display
        first_row = "     ".join([f"{p['first']:>5}" for p in st.session_state.problems])
        second_row = "     ".join([f"{p['operator']}{p['second']:>4}" for p in st.session_state.problems])
        line_row = "     ".join(["-----" for _ in st.session_state.problems])
        answer_row = "     ".join([f"{p['answer']:>5}" for p in st.session_state.problems])
        
        st.code(f"{first_row}\n{second_row}\n{line_row}\n{answer_row}")

if __name__ == "__main__":
    main()