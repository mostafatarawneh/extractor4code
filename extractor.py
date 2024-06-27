import os
import ast

# Function to extract functions from a Python file
def extract_functions_from_file(file_path, function_model_mapping):
    with open(file_path, 'r', encoding='utf-8') as file:
        # Parse the file as an AST
        tree = ast.parse(file.read(), filename=file_path)

        # Extract functions
        function_definitions = [node for node in tree.body if isinstance(node, ast.FunctionDef)]

        # Group functions by model
        functions_by_model = {}
        for function_def in function_definitions:
            for model_name, function_names in function_model_mapping.items():
                if function_def.name in function_names:
                    if model_name not in functions_by_model:
                        functions_by_model[model_name] = []
                    functions_by_model[model_name].append(function_def)

        return functions_by_model

# Function to save functions to module files
def save_functions_to_modules(models, output_directory):
    os.makedirs(output_directory, exist_ok=True)

    for model_name, functions in models.items():
        # Combine all functions related to the model into one module file
        module_file_path = os.path.join(output_directory, f"{model_name}.py")
        
        with open(module_file_path, 'w', encoding='utf-8') as module_file:
            for function in functions:
                # Write function definition to the module file
                function_code = ast.unparse(function)
                module_file.write(function_code)
                module_file.write("\n\n")  # Add newline between functions

# Example usage
if __name__ == "__main__":
    # Mapping of model names to function names
    function_model_mapping = {
        "Logging_Utilities":["setup_logging",
"log_info",
"log_warning",
"log_error",
"log_exception",],
        "Student_Information": ["get_student_statistic_info",
"get_teacher_class_students",
"get_teacher_homeroom_class",
"get_school_classes_and_students_with_classes",
"get_school_students_ids",
"get_class_students",
"get_class_students_ids",
"get_secondery_students",
"get_parents",],
        "Marks_and_Grades_Management":["get_marks",
"get_marks_v2",
"get_school_marks",
"get_school_marks_version_2",
"get_all_AssessmentItemsGradingTypes",
"get_marks_and_names_dictionary_list",
"calculate_percentage",
"create_max_marks_assessments_dictionary",
"create_max_of_dictionaries",
"insert_students_names_and_marks",
"insert_to_side_marks_document_with_marks",
"insert_to_e_side_marks_doc",
"offline_sort_assessement_ids",
"offline_sort_assessement_period_ids_v2",
"get_assessments_periods_dictionary_offline",
"get_assessment_periods_dictionary",
"get_assessments",
"get_editable_assessments",
"get_assessments_periods_data2",
"get_assessment_id_from_grade_id",],
        "File_Handling_and_PDF_Generation":["read_large_json_files",
"read_json_file",
"read_all_xlsx_in_folder",
"save_dictionary_to_json_file",
"convert_files_to_pdf",
"merge_pdfs",
"delete_pdf_page",
"create_zip",
"copy_ods_file",
"delete_file",],
        "Absent_Management":["fill_student_absent_doc_wrapper",
"fill_student_absent_doc_wrapper_with_absent_filled",
"fill_student_absent_A4_doc_wrapper",
"mark_all_students_as_present",
"mark_students_absent_in_dates",
"fill_students_absent_in_dates_wrapper",
"erase_students_absent_dates",
"get_class_absent_days_with_id",
"create_random_absent_list",
"extract_absent_dates_from_text",
"get_school_absent_days_with_studentID_and_countOfAbsentDays_and_classID_and_className",],
        "Assessment_and_Period_Handling":["find_assessment_above_max_for_one_student",
"find_above_max_mark_for_assessments",
"create_max_of_dictionaries",
"offline_sort_assessement_period_ids_v2",
"offline_get_assessment_id_from_grade_id",],
        "Network_and_Web_Utilities":["scrape_schools",
"make_request",
"get_auth",
"get_tor_nodes_with_prefix",
"print_bootstrap_lines",],
        "Document_Manipulation":["convert_official_marks_doc",
"check_file_if_official_marks_file",
"create_coloured_certs_wrapper",
"reorder_official_marks_to_A4",
"fill_official_marks_doc_wrapper_offline",
"fill_official_marks_doc_wrapper",
"fill_official_marks_a3_two_face_doc2_offline_version",
"fill_official_marks_a3_two_face_doc2",
"convert_files_to_pdf",
"convert_to_marks_offline_from_send_folder",
"create_coloured_certs_wrapper",
"create_coloured_certs_excel",
"create_coloured_certs_ods",],
        "Data_Processing":["get_basic_info",
"process_students_info",
"get_subjects_dictionary_list_from_the_site",
"get_class_subjects",
"get_class_subject_teacher_mapping_dictionary",
"get_subject_dictionary",
"get_assessment_periods_list",
"get_assessment_periods_dictionary",
"add_subjects_to_class_data_dic",
"get_school_marks",
"create_excel_from_data",
"calculate_percentage",
"inserted_marks_percentage_from_dataframes_variable",
"create_fuzz_list",],
        "Wrappers":["fill_student_absent_doc_wrapper",
"fill_student_absent_doc_wrapper_with_absent_filled",
"fill_student_absent_A4_doc_wrapper",
"insert_students_names_in_excel_marks",
"fill_official_marks_doc_wrapper_offline",
"fill_official_marks_doc_wrapper",
"fill_official_marks_a3_two_face_doc2_offline_version",
"fill_official_marks_a3_two_face_doc2",
"teachers_marks_upload_percentage_wrapper",
"teachers_marks_upload_percentage",
"side_marks_document_with_marks",
"Read_E_Side_Note_Marks_ods",
"Read_E_Side_Note_Marks_xlsx",
"enter_marks_arbitrary_controlled_version",
"enter_marks_arbitrary",],
        "Utilities":["playsound",
"group_students",
"get_students_info_subjectsMarks",
"generate_numbers",
"check_sum",
"generate_numbers_with_sum",
"convert_to_ranges",
"calculate_age",
"convert_avarage_to_words",
"score_in_words",
"add_averages_to_group_list",
"add_subject_sum_dictionary",
"chunks",
"print_page_pairs",
"five_names_every_class_wrapper",
"five_names_every_class",
"convert_official_marks_doc",
"teachers_marks_upload_percentage_wrapper",
"teachers_marks_upload_percentage",
"side_marks_document_with_marks",
"merge_pdfs",
"get_pdf_files",
"create_zip",
"Read_E_Side_Note_Marks_ods",
"upload_marks",
"get_school_load",
"get_school_teachers",
"get_school_teachers_load",
"count_teachers_grades",
"get_teacher_load_with_name",
"count_teacher_load",
"create_tables_wrapper",
"create_certs_wrapper",
"create_tables",
"create_certs",
"create_coloured_certs_excel",
"create_coloured_certs_ods",
"sort_dictionary_list_based_on",
"convert_avarage_to_words",
"score_in_words",
"add_averages_to_group_list",
"add_subject_sum_dictionary",
"playsound",
"group_students",
"get_students_info_subjectsMarks",
"get_school_students_ids",
"fill_official_marks_a3_two_face_doc2_offline_version",
"Read_E_Side_Note_Marks_xlsx",
"enter_marks_arbitrary_controlled_version",
"get_editable_assessments",
"assessments_periods_min_max_mark",
"get_all_assessments_periods_data2",
"enter_marks_arbitrary",
"get_class_students_ids",
"get_required_data_to_enter_marks",
"get_grade_info",
"get_grade_name_from_grade_id",
"get_assessment_id_from_grade_id",
"create_e_side_marks_doc",
"split_A3_pages",
"reorder_official_marks_to_A4",
"delete_files_except",
"delete_empty_rows",
"delete_file",
"copy_ods_file",
"get_class_short",
"get_students_marks",
"get_assessments_periods",
"get_all_assessments_periods",
"get_assessments_id",
"get_AcademicTerms",
"draw_rect_top",
"draw_rect_bottom",
"draw_rect_left",
"draw_rect_right",
"add_margins",
"mawad",
"get_basic_info",
"fill_custom_shape",
"clear_text_custom_shape",
"get_sheet_custom_shapes",
"get_ods_sheets",
"page_counter_official_marks_doc_a3_two_face",
"generate_pdf",
"word2pdf",
"fill_doc",
"word_variables",
"my_jq",
"make_request",
"get_auth",
"inst_name",
"inst_area",
"user_info",
"get_teacher_classes1",
"get_teacher_classes2",
"get_class_students",
"enter_mark",
"get_curr_period",
"get_assessments",
"get_sub_info",
"side_marks_document",
"insert_students_names_in_excel_marks",
"delete_empty_rows",
"read_excel_marks",
"insert_students_names_and_marks",
"create_excel_sheets_marks",
"count_files",
"delete_send_folder",
"get_students_marks",
"sort_send_folder_into_two_folders",
"extract_primary_and_other_classes",],
        # Add more models and corresponding function names as needed
    }

    # Path to the Python file
    file_path = "/home/kali/school_telgram_bot/telegram_bot/utils1.py"

    # Extract functions from the file based on the mapping
    models = extract_functions_from_file(file_path, function_model_mapping)

    # Save functions to modules
    output_directory = "./EmisHub_Modules"
    save_functions_to_modules(models, output_directory)

    print(f"Functions extracted and saved to '{output_directory}' directory.")
