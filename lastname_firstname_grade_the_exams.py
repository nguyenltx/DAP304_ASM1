import re
import os
import statistics
# Định nghĩa mẫu id học sinh chuẩn
id_pattern = re.compile(r'^N\d{8}$')

# Task 1, định nghĩa hàm open file
def open_file(file_to_open):
    try:
        # Mở file
        with open(file_to_open, 'r') as file:
            print('Successfully opened ' + file_name)
        return True # Mở thành công
    except FileNotFoundError:
        print('File cannot be found. Please try again.')
        return False # Không tìm thấy file

# Task 2, định nghĩa hàm check file
def check_file(file_to_check):
    print('\n**** ANALYZING ****\n')
    # Mở tệp và đọc nội dung
    with open(file_to_check,'r') as file:
        lines = file.readlines()

    # Tổng số dòng trong tệp
    total_lines = len(lines)
    print(f'Total lines in the {file_name}: {total_lines} lines')

    # Biến đếm số dòng không hợp lệ
    invalid_lines = 0

    # Duyệt từng dòng để kiểm tra tính hợp lệ, đầu tiên là split theo dấu phẩy
    for i, line in enumerate(lines):
        parts = line.split(',')
        # Kiểm tra tổng số giá trị trong từng dòng
        if len(parts) != 26:
            print('Invalid line of data: does not contain exactly 26 values:\n', line)
            invalid_lines += 1
        # Kiểm tra id học sinh đúng định dạng
        student_id = parts[0]
        if not id_pattern.match(student_id):
            print('Invalid line of data: N# is invalid\n', line)
            invalid_lines += 1

    # Báo cáo số dòng không hợp lệ
    print(f'Total invalid lines in the {file_name}: {invalid_lines} lines')

# Task 3 chấm điểm học sinh
# Đáp án chuẩn
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_key_part = answer_key.split(',')
# Các bộ đếm
scores = [] # list để lưu điểm các học sinh
skipped_count = [0] * 25 # list đếm số câu hỏi bị bỏ qua tương ứng 25 câu hỏi
incorrect_count = [0] * 25 # list đếm số câu hỏi bị trả lời sai

# Định nghĩa hàm chấm điểm
def score_file(file_to_score):
    # Mở tệp và đọc nội dung
    with open(file_to_score,'r') as file:
        lines = file.readlines()
    # Duyệt qua từng dòng
    for line in lines:
        data = line.split(',')
        # Kiểm tra tính hợp lệ của dòng: 26 tp, bắt đầu với mã hs và sau đó là chữ
        if len(data) != 26 or not id_pattern.match(data[0]):
            continue
        # Lưu ID học sinh cho task 4
        student_id = data[0]
        student_ids.append(student_id)
        # Chấm điểm học sinh
        student_answers = [x.strip() for x in data[1:]] # phần tử cuối trong mỗi dòng có \n nên dùng strip để loại bỏ nó
        score = 0
        for j, answer in enumerate(student_answers):
            if answer == answer_key_part[j]: # nếu đáp án đúng
                score += 4
            elif answer == '': # nếu bỏ qua
                skipped_count[j] += 1
            else: # còn lại là đáp án sai
                score -= 1
                incorrect_count[j] += 1
        scores.append(score) # điểm của từng hs được ghi vào scores
    # Thống kê
    # Số lượng học sinh đạt điểm cao (>80)
    high_scores = 0
    for i in scores:
        if i > 80:
            high_scores += 1
    # Điểm trung bình
    avg_score = round(statistics.mean(scores), 3)
    # Điểm cao nhất
    max_score = max(scores)
    # Điểm thấp nhất
    min_score = min(scores)
    # Miền giá trị điểm
    score_range = max_score - min_score
    # Giá trị trung vị
    median_score = round(statistics.median(scores), 3)
    # Câu hỏi bị bỏ qua nhiều nhất
    most_skipped_questions = []
    for i, count in enumerate(skipped_count):
        if count == max(skipped_count):
            skip_rate = round(count / len(scores), 3)
            most_skipped_questions.append((i+1, count, skip_rate))
    # Câu hỏi bị trả lời sai nhiều nhất
    most_incorrect_questions = []
    for i, count in enumerate(incorrect_count):
        if count == max(incorrect_count):
            incorrect_rate = round(count / len(scores), 3)
            most_incorrect_questions.append((i+1, count, incorrect_rate))

    # In kết quả thống kê
    print('\n**** REPORT ****\n')
    print(f'Total students of high scores: {high_scores}')
    print(f'Average scores: {avg_score}')
    print(f'Highest score: {max_score}')
    print(f'Lowest score: {min_score}')
    print(f'Range of scores: {score_range}')
    print(f'Median scores: {median_score}')
    print('Most skipped questions:')
    for question, count, rate in most_skipped_questions:
        print(f'Question: {question}, skipped count: {count}, rate {rate*100}%')
    print('Most incorrect questions:')
    for question, count, rate in most_incorrect_questions:
        print(f'Question: {question}, incorrect count: {count}, rate {rate*100}%')
# Task 4
# Tạo list chứa student ids
student_ids = []
# Định nghĩa hàm write file
def write_file(file_to_write):
    output_file = file_to_write.replace('.txt', '_grade.txt')
    with open(output_file,'w') as file:
        for student_id, score in zip(student_ids, scores):
            file.write(f'{student_id},{score}\n')
    print(f'Results written to {output_file}')

# Chương trình chính
while True:
    # Nhập tên file
    file_name = input('Enter a class file to grade (i.e. class1 for class1.txt): ') + '.txt'
    file_path = os.path.join('Data Files', file_name)
    # Kiểm tra mở file
    if open_file(file_path):   
        # chạy các function nếu mở file thành công
        try:
            check_file(file_path)
            score_file(file_path)
            write_file(file_path)
        except Exception as err:
            print(f'An error found!: {err}')
        # Hỏi người dùng có tiếp tục check file khác không
        while True:
            user_input = input('Do you want to check another file?(yes/no): ')
            if user_input == 'yes':
                break
            elif user_input == 'no':
                print('Good bye!')
                exit()
            else:
                print("Invalid input, please enter 'yes' or 'no'.")
    else:
        # Nếu open file false thì sẽ nhập lại tên file
        continue