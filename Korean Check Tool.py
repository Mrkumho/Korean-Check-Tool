#!/usr/bin/env python
# coding: utf-8

# In[14]:


import tkinter as tk
from tkinter import filedialog, ttk
from docx import Document
import pandas as pd
import re

def find_korean_in_word(file_path, show_chars):
    """워드 파일 내 한글 위치 탐색 (체크박스 상태 반영)"""
    doc = Document(file_path)
    results = []
    korean_pattern = re.compile('[가-힣ㄱ-ㅎㅏ-ㅣ]')
    
    for para_idx, para in enumerate(doc.paragraphs):
        line_text = para.text
        if show_chars:
            # 문자 단위 상세 분석
            for char_idx, char in enumerate(line_text):
                if korean_pattern.match(char):
                    results.append(
                        f"📄 Word 파일 [{file_path}]\n"
                        f"    → 문단 {para_idx+1}번, 문자 {char_idx+1}번\n"
                        f"    → 내용: '{line_text}'\n"
                        f"    → 발견 문자: '{char}'\n"
                    )
        else:
            # 문단 단위 요약 분석
            if korean_pattern.search(line_text):
                results.append(
                    f"📄 Word 파일 [{file_path}]\n"
                    f"    → 문단 {para_idx+1}번\n"
                    f"    → 내용: '{line_text}'\n"
                )
    return results

def find_korean_in_excel(file_path, show_chars):
    """엑셀 파일 내 한글 위치 탐색 (체크박스 상태 반영)"""
    results = []
    korean_pattern = re.compile('[가-힣ㄱ-ㅎㅏ-ㅣ]')
    
    xls = pd.ExcelFile(file_path)
    for sheet_name in xls.sheet_names:
        sheet_df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
        
        for row_idx, row in sheet_df.iterrows():
            for col_idx, cell in enumerate(row):
                if pd.isna(cell):
                    continue
                cell_str = str(cell)
                if show_chars:
                    # 문자 단위 상세 분석
                    for char_idx, char in enumerate(cell_str):
                        if korean_pattern.match(char):
                            results.append(
                                f"📊 Excel 파일 [{file_path}]\n"
                                f"    → 시트: {sheet_name}\n"
                                f"    → 위치: {row_idx+1}행 {col_idx+1}열\n"
                                f"    → 내용: '{cell_str}'\n"
                                f"    → 발견 문자: '{char}'\n"
                            )
                else:
                    # 셀 단위 요약 분석
                    if korean_pattern.search(cell_str):
                        results.append(
                            f"📊 Excel 파일 [{file_path}]\n"
                            f"    → 시트: {sheet_name}\n"
                            f"    → 위치: {row_idx+1}행 {col_idx+1}열\n"
                            f"    → 내용: '{cell_str}'\n"
                        )
    return results

def open_word_file():
    file_path = filedialog.askopenfilename(filetypes=[("Word Files", "*.docx")])
    if file_path:
        result_text.delete(1.0, tk.END)
        results = find_korean_in_word(file_path, show_chars_var.get())
        if results:
            for res in results:
                result_text.insert(tk.END, res + "\n" + "-"*50 + "\n")
        else:
            result_text.insert(tk.END, "⚠️ 한글 문자가 발견되지 않았습니다.")

def open_excel_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx *.xls")])
    if file_path:
        result_text.delete(1.0, tk.END)
        results = find_korean_in_excel(file_path, show_chars_var.get())
        if results:
            for res in results:
                result_text.insert(tk.END, res + "\n" + "-"*50 + "\n")
        else:
            result_text.insert(tk.END, "⚠️ 한글 문자가 발견되지 않았습니다.")

# GUI 설정
root = tk.Tk()
root.title("🔍 한글 탐지기 - 스마트 옵션 시스템")
root.geometry("800x600")

# 체크박스 변수
show_chars_var = tk.BooleanVar(value=False)

# 상단 컨트롤 프레임
control_frame = ttk.Frame(root)
control_frame.pack(pady=10)

# 옵션 체크박스
check_button = ttk.Checkbutton(
    control_frame,
    text="발견 문자 상세 표시",
    variable=show_chars_var
)
check_button.pack(side=tk.LEFT, padx=10)

# 파일 선택 버튼 프레임
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

btn_style = {'width': 20}
btn_word = ttk.Button(
    button_frame,
    text="📝 워드 파일 분석",
    command=open_word_file,
    **btn_style
)
btn_word.pack(side=tk.LEFT, padx=5)

btn_excel = ttk.Button(
    button_frame,
    text="📊 엑셀 파일 분석",
    command=open_excel_file,
    **btn_style
)
btn_excel.pack(side=tk.LEFT, padx=5)

# 결과 출력 영역
result_text = tk.Text(
    root,
    wrap=tk.WORD,
    font=('Malgun Gothic', 10),
    padx=10,
    pady=10
)
result_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()

