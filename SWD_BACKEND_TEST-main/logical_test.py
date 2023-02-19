
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""




def Convert_Number_To_Thai_text()-> str:
    num_thai_text = {
                        '-': "ลบ",'.': "จุด",0  : "ศูนย์",1  : "หนึ่ง",
                        2  : "สอง",3  : "สาม",4  : "สี่",5  : "ห้า",
                        6  : "หก",7  : "เจ็ด",8  : "แปด",9  : "เก้า"
                    }



    deci = {
        0:'ศูนย์',2:"ยี่สิบ",3:"สามสิบ",4:"สี่สิบ",5:"ห้าสิบ",
        6:"หกสิบ",7:"เจ็ดสิบ",8:"แปดสิบ",9:"เก้าสิบ"
    }

    one_edd = {
        1:"เอ็ด"
    }



    million_text_num = 'ล้าน'
    onehundredthousand_text_num = 'แสน'
    tenthousand_text_num = 'หมื่น'
    thousand_text_num = 'พัน'
    hundred_text_num = 'ร้อย'
    ten_text_num = 'สิบ'
    print('Convert Number to Thai Text')
    num = str(input('Number That You Want To Convert to Thai Text : '))
    if  0 <= int(num) < 10000000 :
        len_num = len(num)
        if len_num == 7 :
            if num[0] == '0' :
                print('num cant be zero')

            else :
                first_digit = f'{num_thai_text[int(num[0])]}{million_text_num}'
                second_digit = f'{num_thai_text[int(num[1])]}{onehundredthousand_text_num}'
                third_digit = f'{num_thai_text[int(num[2])]}{tenthousand_text_num}'
                forth_digit = f'{num_thai_text[int(num[3])]}{thousand_text_num}'
                fifth_digit = f'{num_thai_text[int(num[4])]}{hundred_text_num}'
                if num[5] == '1' :
                    sixth_digit = f'{ten_text_num}'
                    if num[6] == '1' :
                        seventh_digit = f'{one_edd[int(num[6])]}'

                    else : 
                        seventh_digit = f'{num_thai_text[int(num[6])]}'


                else :
                    sixth_digit = f'{deci[int(num[5])]}'
                    if num[6] == '1' :
                        seventh_digit = f'{one_edd[int(num[6])]}'

                    else : 
                        seventh_digit = f'{num_thai_text[int(num[6])]}'

                result = first_digit+second_digit+third_digit+forth_digit+fifth_digit+sixth_digit+seventh_digit
                result1 = result.replace('ศูนย์เอ็ด','หนึ่ง')
                result2 = result1.replace('ศูนย์สิบ','')
                result3 = result2.replace('ศูนย์ร้อย','')
                result4 = result3.replace('ศูนย์พัน','')
                result5 = result4.replace('ศูนย์หมื่น','')
                result6 = result5.replace('ศูนย์แสน','')
                return result6

        
        elif len_num == 6 :
            if num[0] == '0' :
                print('num cant be zero')

            else :
                first_digit = f'{num_thai_text[int(num[0])]}{onehundredthousand_text_num}'
                second_digit = f'{num_thai_text[int(num[1])]}{tenthousand_text_num}'
                third_digit = f'{num_thai_text[int(num[2])]}{thousand_text_num}'
                forth_digit = f'{num_thai_text[int(num[3])]}{hundred_text_num}'
                if num[4] == '1' :
                    fifth_digit = f'{ten_text_num}'
                    if num[5] == '1' :
                        sixth_digit = f'{one_edd[int(num[5])]}'

                    else : 
                        sixth_digit = f'{num_thai_text[int(num[5])]}'


                else :
                    fifth_digit = f'{deci[int(num[4])]}'
                    if num[5] == '1' :
                        sixth_digit = f'{one_edd[int(num[5])]}'

                    else : 
                        sixth_digit = f'{num_thai_text[int(num[5])]}'

                result = first_digit+second_digit+third_digit+forth_digit+fifth_digit+sixth_digit
                result1 = result.replace('ศูนย์เอ็ด','หนึ่ง')
                result2 = result1.replace('ศูนย์สิบ','')
                result3 = result2.replace('ศูนย์ร้อย','')
                result4 = result3.replace('ศูนย์พัน','')
                result5 = result4.replace('ศูนย์หมื่น','')
                result6 = result5.replace('ศูนย์แสน','')
                return result6

        elif len_num == 5 :
            if num[0] == '0' :
                print('num cant be zero')

            else :
                first_digit = f'{num_thai_text[int(num[0])]}{tenthousand_text_num}'
                second_digit = f'{num_thai_text[int(num[1])]}{thousand_text_num}'
                third_digit = f'{num_thai_text[int(num[2])]}{hundred_text_num}'
                if num[3] == '1' :
                    forth_digit = f'{ten_text_num}'
                    if num[4] == '1' :
                        fifth_digit = f'{one_edd[int(num[4])]}'

                    else : 
                        fifth_digit = f'{num_thai_text[int(num[4])]}'


                else :
                    forth_digit = f'{deci[int(num[3])]}'
                    if num[4] == '1' :
                        fifth_digit = f'{one_edd[int(num[4])]}'

                    else : 
                        fifth_digit = f'{num_thai_text[int(num[4])]}'
                result = first_digit+second_digit+third_digit+forth_digit+fifth_digit
                result1 = result.replace('ศูนย์เอ็ด','หนึ่ง')
                result2 = result1.replace('ศูนย์สิบ','')
                result3 = result2.replace('ศูนย์ร้อย','')
                result4 = result3.replace('ศูนย์พัน','')
                result5 = result4.replace('ศูนย์หมื่น','')
                result6 = result5.replace('ศูนย์แสน','')
                return result6
                

        elif len_num == 4 :
            if num[0] == '0' :
                print('num cant be zero')

            else :
                first_digit = f'{num_thai_text[int(num[0])]}{thousand_text_num}'
                second_digit = f'{num_thai_text[int(num[1])]}{hundred_text_num}'
                if num[2] == '1' :
                    third_digit = f'{ten_text_num}'
                    if num[3] == '1' :
                        forth_digit = f'{one_edd[int(num[3])]}'

                    else : 
                        forth_digit = f'{num_thai_text[int(num[3])]}'


                else :
                    third_digit = f'{deci[int(num[2])]}'
                    if num[3] == '1' :
                        forth_digit = f'{one_edd[int(num[3])]}'

                    else : 
                        forth_digit = f'{num_thai_text[int(num[3])]}'
                result = first_digit+second_digit+third_digit+forth_digit
                result1 = result.replace('ศูนย์เอ็ด','หนึ่ง')
                result2 = result1.replace('ศูนย์สิบ','')
                result3 = result2.replace('ศูนย์ร้อย','')
                result4 = result3.replace('ศูนย์พัน','')
                result5 = result4.replace('ศูนย์หมื่น','')
                result6 = result5.replace('ศูนย์แสน','')
                return result6

        elif len_num == 3 :
            if num[0] == '0' :
                print('num cant be zero')

            else :
                first_digit = f'{num_thai_text[int(num[0])]}{hundred_text_num}'
                if num[1] == '1' :
                    second_digit = f'{ten_text_num}'
                    if num[2] == '1' :
                        third_digit = f'{one_edd[int(num[2])]}'

                    else : 
                        third_digit = f'{num_thai_text[int(num[2])]}'


                else :
                    second_digit = f'{deci[int(num[1])]}'
                    if num[2] == '1' :
                        third_digit = f'{one_edd[int(num[2])]}'

                    else : 
                        third_digit = f'{num_thai_text[int(num[2])]}'
                result = first_digit+second_digit+third_digit
                result1 = result.replace('ศูนย์เอ็ด','หนึ่ง')
                result2 = result1.replace('ศูนย์สิบ','')
                result3 = result2.replace('ศูนย์ร้อย','')
                result4 = result3.replace('ศูนย์พัน','')
                result5 = result4.replace('ศูนย์หมื่น','')
                result6 = result5.replace('ศูนย์แสน','')
                return result6

        elif len_num == 2 :
            if num[0] == '0' :
                print('num cant be zero')

            else :
                if num[0] == '1' :
                    first_digit = f'{ten_text_num}'
                    if num[1] == '1' :
                        second_digit = f'{one_edd[int(num[1])]}'

                    else : 
                        second_digit = f'{num_thai_text[int(num[1])]}'

                else :
                    first_digit = f'{deci[int(num[0])]}'
                    if num[1] == '1' :
                        second_digit = f'{one_edd[int(num[1])]}'

                    else : 
                        second_digit = f'{num_thai_text[int(num[1])]}'

                result = first_digit+second_digit
                result1 = result.replace('ศูนย์เอ็ด','หนึ่ง')
                result2 = result1.replace('ศูนย์สิบ','')
                result3 = result2.replace('ศูนย์ร้อย','')
                result4 = result3.replace('ศูนย์พัน','')
                result5 = result4.replace('ศูนย์หมื่น','')
                result6 = result5.replace('ศูนย์แสน','')
                return result6

        elif len_num == 1 :

            first_digit = f'{num_thai_text[int(num[0])]}'

            result = first_digit
        
            result1 = result.replace('ศูนย์เอ็ด','หนึ่ง')
            result2 = result1.replace('ศูนย์สิบ','')
            result3 = result2.replace('ศูนย์ร้อย','')
            result4 = result3.replace('ศูนย์พัน','')
            result5 = result4.replace('ศูนย์หมื่น','')
            result6 = result5.replace('ศูนย์แสน','')
            return result6

    else :
        return 'Number Not In Range'

print(Convert_Number_To_Thai_text())