import streamlit as st
import time

# Set up the page
st.set_page_config(page_title="Math Buddy", page_icon="🧮", layout="wide")

# Initialize session state
if 'problems' not in st.session_state:
    st.session_state.problems = []
if 'current_problem' not in st.session_state:
    st.session_state.current_problem = None
if 'show_popup' not in st.session_state:
    st.session_state.show_popup = False
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

def create_problem(operator, first_num, second_num):
    """Create a new math problem"""
    op_symbols = {
        'addition': '+',
        'subtraction': '-',
        'multiplication': '×',
        'division': '÷'
    }
    
    if operator == 'addition':
        correct_answer = first_num + second_num
    elif operator == 'subtraction':
        correct_answer = first_num - second_num
    elif operator == 'multiplication':
        correct_answer = first_num * second_num
    elif operator == 'division':
        if second_num == 0:
            return None
        correct_answer = first_num / second_num
    
    return {
        'first': first_num,
        'operator': op_symbols[operator],
        'second': second_num,
        'answer': correct_answer,
        'op_type': operator
    }

def show_confetti():
    """Display confetti animation"""
    st.balloons()

def main():
    # Header with emoji
    st.title("🧮 FIRST FOUR Pre-School")
    st.header("✨ Math Buddy ✨")
    st.divider()
    
    # Instructions
    st.info("**Choose an operation below and solve the problem!**")
    
    # Main layout
    col_left, col_right = st.columns([3, 2])
    
    with col_left:
        st.subheader("Choose Your Operation:")
        
        # Four colorful operation buttons in a row
        btn_col1, btn_col2, btn_col3, btn_col4 = st.columns(4)
        
        operation_selected = None
        
        with btn_col1:
            if st.button("➕ Addition", use_container_width=True, type="primary"):
                operation_selected = 'addition'
                st.session_state.show_popup = False
                st.session_state.attempts = 0
        
        with btn_col2:
            if st.button("➖ Subtraction", use_container_width=True, type="secondary"):
                operation_selected = 'subtraction'
                st.session_state.show_popup = False
                st.session_state.attempts = 0
        
        with btn_col3:
            if st.button("✖️ Multiplication", use_container_width=True, type="primary"):
                operation_selected = 'multiplication'
                st.session_state.show_popup = False
                st.session_state.attempts = 0
        
        with btn_col4:
            if st.button("➗ Division", use_container_width=True, type="secondary"):
                operation_selected = 'division'
                st.session_state.show_popup = False
                st.session_state.attempts = 0
        
        st.divider()
        
        # If an operation is selected, show input fields
        if operation_selected or st.session_state.current_problem:
            if operation_selected:
                st.session_state.current_problem = operation_selected
            
            op = st.session_state.current_problem
            
            st.subheader(f"Enter Numbers for {op.title()}:")
            
            # Different labels based on operation
            if op == 'addition':
                first_num = st.number_input("Enter Augend (first number):", value=0, step=1, key="first")
                second_num = st.number_input("Enter Addend (second number):", value=0, step=1, key="second")
            elif op == 'subtraction':
                first_num = st.number_input("Enter Minuend (first number):", value=0, step=1, key="first")
                second_num = st.number_input("Enter Subtrahend (second number):", value=0, step=1, key="second")
            elif op == 'multiplication':
                first_num = st.number_input("Enter Multiplier (first number):", value=0, step=1, key="first")
                second_num = st.number_input("Enter Multiplicand (second number):", value=0, step=1, key="second")
            else:  # division
                first_num = st.number_input("Enter Dividend (first number):", value=0, step=1, key="first")
                second_num = st.number_input("Enter Divisor (second number):", value=1, step=1, key="second")
            
            # Create the problem
            problem = create_problem(op, first_num, second_num)
            
            if problem is None:
                st.error("⚠️ ERROR: You can't divide a number by zero!")
            else:
                # Show the problem
                st.markdown("### Solve This:")
                st.code(f"  {problem['first']}\n{problem['operator']} {problem['second']}\n-----\n  ?")
                
                # Answer input
                user_answer = st.number_input("Your Answer:", value=0, step=1, key="user_answer")
                
                # Check answer button
                if st.button("🎯 Submit Answer", use_container_width=True, type="primary"):
                    st.session_state.attempts += 1
                    
                    # Check if correct
                    try:
                        if op == 'division':
                            is_correct = abs(float(user_answer) - problem['answer']) < 0.01
                        else:
                            is_correct = int(user_answer) == int(problem['answer'])
                        
                        if is_correct:
                            # Correct answer!
                            show_confetti()
                            st.success(f"🎉 Correct Answer! Great job! (Attempts: {st.session_state.attempts})")
                            
                            # Add to history
                            st.session_state.problems.append(problem)
                            
                            # Reset
                            time.sleep(1)
                            st.session_state.current_problem = None
                            st.session_state.attempts = 0
                            st.rerun()
                        else:
                            # Wrong answer - show popup
                            st.session_state.show_popup = True
                    except:
                        st.error("Please enter a valid number!")
                
                # Show popup for wrong answer
                if st.session_state.show_popup:
                    st.error(f"❌ Incorrect answer! (Attempt {st.session_state.attempts})")
                    
                    popup_col1, popup_col2 = st.columns(2)
                    
                    with popup_col1:
                        if st.button("🔄 Try Again", use_container_width=True, type="primary"):
                            st.session_state.show_popup = False
                            st.rerun()
                    
                    with popup_col2:
                        if st.button("💡 Show Correct Answer", use_container_width=True):
                            st.info(f"The correct answer is: **{problem['answer']}**")
                            st.session_state.show_popup = False
                            
                            # Add to history even if they gave up
                            st.session_state.problems.append(problem)
                            
                            # Reset after showing answer
                            if st.button("➡️ Next Problem"):
                                st.session_state.current_problem = None
                                st.session_state.attempts = 0
                                st.rerun()
        else:
            st.info("👆 Click one of the operation buttons above to start!")
    
    with col_right:
        st.subheader("📊 Problem History")
        
        if st.session_state.problems:
            st.write(f"**Total Problems Solved:** {len(st.session_state.problems)}")
            
            # Clear history button
            if st.button("🗑️ Clear History", use_container_width=True):
                st.session_state.problems = []
                st.rerun()
            
            st.write("---")
            
            # Display recent problems
            for idx, prob in enumerate(reversed(st.session_state.problems[-5:]), 1):
                with st.container():
                    st.markdown(f"**Problem {len(st.session_state.problems) - idx + 1}:**")
                    st.code(f"  {prob['first']}\n{prob['operator']} {prob['second']}\n-----\n  {prob['answer']}")
            
            if len(st.session_state.problems) > 5:
                st.caption(f"... and {len(st.session_state.problems) - 5} more problems")
        else:
            st.write("No problems solved yet!")
            st.write("Start solving to build your history. 🚀")
    
    # Show all problems at the bottom
    if st.session_state.problems:
        st.divider()
        st.subheader("📝 All Your Work:")
        
        # Create formatted display
        first_row = "     ".join([f"{p['first']:>5}" for p in st.session_state.problems])
        second_row = "     ".join([f"{p['operator']}{p['second']:>4}" for p in st.session_state.problems])
        line_row = "     ".join(["-----" for _ in st.session_state.problems])
        answer_row = "     ".join([f"{p['answer']:>5}" for p in st.session_state.problems])
        
        st.code(f"{first_row}\n{second_row}\n{line_row}\n{answer_row}")

if __name__ == "__main__":
    main()