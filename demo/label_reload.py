# -*- coding:utf-8 -*-
import json

def main():
    bullet_path = 'demo/predict.label'
    input_json = 'demo/input.json'
    output_json = 'demo/output.json'
    ERROR_CASE_OUTPUT = 1
    error_case_path = 'demo/error_case.json'

    if ERROR_CASE_OUTPUT == 1:
        error_case_stream = open(error_case_path, 'w')
        error_case = []
        error_case_num = 0

    bullet_stream = open(bullet_path, 'r')
    input_stream = open(input_json, 'r')
    output_stream = open(output_json, 'w')
    guns = json.load(input_stream)
    bullets = bullet_stream.readlines()
    for i in range(len(bullets)):
        bullet = bullets[i].strip()
        if bullet == u'非影视作品':
            if (ERROR_CASE_OUTPUT == 1) and (guns[i]['DL'] != bullet):
                error_case.append(guns[i])
                error_case[error_case_num]['labeled as'] = bullet
                error_case_num += 1
            guns[i]['DL'] = bullet
        else:
            guns[i]['DL'] = '影视作品'
            guns[i]['XL'] = bullet
            if (ERROR_CASE_OUTPUT == 1) and (guns[i]['XL'] != bullet):
                error_case.append(guns[i])
                error_case[error_case_num]['labeled as'] = bullet
                error_case_num += 1
    json.dump(guns, output_stream)
    json.dump(error_case, error_case_stream)
    output_stream.close()
    error_case_stream.close()

if __name__ == '__main__':
    main()