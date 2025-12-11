import time

## 🛠️ ส่วนที่ 1: การ Implement Algorithm Sorting

from sorting_algorithms_quick_sort import quick_sort

from sorting_algorithms_bubble_sort import bubble_sort

## ⚙️ ส่วนที่ 2: การจัดการ Input และการเลือก Algorithm

def get_user_input_and_select_algorithm():
    """
    Handles user input for the list of numbers and the choice of sorting algorithm.
    Returns the list, the selected sorting function, and its name.
    """
    print("--- Sorting Algorithm Selector (Python) ---")
    
    # 1. รับ Input รายการตัวเลข
    while True:
        try:
            # Prompt the user to input numbers, accepting space or comma separated values
            input_list_str = input("ป้อนรายการตัวเลข (คั่นด้วยช่องว่าง/comma): ")
            
            # Clean up the input (replace comma with space, then split)
            clean_str = input_list_str.replace(',', ' ')
            
            # Convert list of strings to list of integers, ignoring non-numeric entries
            data_list = [int(x) for x in clean_str.split() if x.strip().lstrip('-').isdigit()]
            
            if not data_list:
                 print("⚠️ กรุณาป้อนตัวเลขที่ถูกต้องอย่างน้อยหนึ่งตัว")
                 continue
                 
            print(f"✅ ข้อมูลที่คุณป้อน: {data_list}")
            break
        except ValueError:
            # This should generally not be reached due to the isdigit check, but kept for robustness
            print("⚠️ รูปแบบข้อมูลไม่ถูกต้อง กรุณาป้อนเฉพาะตัวเลขเท่านั้น")

    # 2. การเลือก Algorithm
    print("\nเลือก Algorithm ที่ต้องการใช้:")
    print("1. Quick Sort (แนะนำ: เหมาะสำหรับข้อมูลขนาดใหญ่/ประสิทธิภาพสูง)")
    print("2. Bubble Sort (เข้าใจง่าย: เหมาะสำหรับข้อมูลขนาดเล็ก/การศึกษา)")

    algorithm_map = {
        '1': quick_sort,
        '2': bubble_sort
    }
    
    while True:
        choice = input("ป้อนหมายเลข (1 หรือ 2): ")
        if choice in algorithm_map:
            # Get the selected function and determine the algorithm name
            selected_algorithm = algorithm_map.get(choice)
            algorithm_name = "Quick Sort" if choice == '1' else "Bubble Sort"
            print(f"✅ คุณเลือก: **{algorithm_name}**")
            break
        else:
            print("⚠️ กรุณาเลือกหมายเลข 1 หรือ 2 เท่านั้น")
            
    # Return a COPY of the list to ensure the original input remains unchanged for display
    return data_list.copy(), selected_algorithm, algorithm_name


## 🚀 ส่วนที่ 3: Main Function (Integration)

def main():
    """
    The main function to integrate input, selection, and sorting execution.
    """
    
    # 1. จัดการ Input และการเลือก Algorithm
    original_list, sort_function, algorithm_name = get_user_input_and_select_algorithm()
    
    # 2. การเรียกใช้งาน (Integration) และการวัดเวลา
    print("\n--- เริ่มการจัดเรียง ---")
    
    start_time = time.time()
    
    # เรียกใช้ฟังก์ชัน Sorting ที่ถูกเลือก
    sorted_list = sort_function(original_list) 
    
    end_time = time.time()
    
    # Calculate execution time
    execution_time = (end_time - start_time) * 1000 # Convert to milliseconds (ms)
    
    # 3. แสดงผลลัพธ์
    print(f"\n✨ ผลลัพธ์ที่ได้จากการจัดเรียงด้วย **{algorithm_name}**:")
    print(f"  รายการเดิม: {original_list}")
    print(f"  รายการที่จัดเรียงแล้ว: {sorted_list}")
    print(f"  เวลาที่ใช้ในการจัดเรียง: {execution_time:.4f} ms")
    print("--- สิ้นสุดการทำงาน ---")

if __name__ == "__main__":
    main()