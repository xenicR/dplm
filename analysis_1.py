# monosyl inits
# monosyl fins

import re
import operator
import time
start_time = time.time()

# делает списки односложных слов
def M_1():

    #f = open('ipa_lexemes_russian.tsv')
    #f = open('ipa_wordforms_russian.tsv')
    #f = open('ipa_lexemes_macedonian.tsv')
    f = open('ipa_wordforms_polish.tsv')

    f_lines = f.readlines()
    f_lines = f_lines[1:]

    #f_norm = open('monosyllabic_russian_lexemes.tsv', 'w')
    #f_norm = open('monosyllabic_russian_wordforms.tsv', 'w')
    #f_norm = open('monosyllabic_macedonian_lexemes.tsv', 'w')
    f_norm = open('monosyllabic_polish_wordforms.tsv', 'w')

    #f_norm.write('monosyllabic_russian_lexemes' + '\n')
    #f_norm.write('monosyllabic_russian_wordforms' + '\n')
    #f_norm.write('monosyllabic_macedonian_lexemes' + '\n')
    f_norm.write('monosyllabic_polish_wordforms' + '\n')

    for line in f_lines:
        i = 0
        for elem in line:
            if elem == 'V':
                i += 1
        if i == 1:
            f_norm.write(line)


        #if 'V' not in line:
        #    # f_norm.write(line)
        #    print(line)

    f_norm.close()

# делат списки сейчас решим чего — инициалей и финалей односложных слов
def M_2():
    #f = open('monosyllabic_russian_lexemes.tsv')
    #f = open('monosyllabic_russian_wordforms.tsv')
    #f = open('monosyllabic_macedonian_lexemes.tsv')
    f = open('monosyllabic_polish_wordforms.tsv')

    f_lines = f.readlines()
    f_lines = f_lines[1:]  # РАБОЧАЯ ВЕРСИЯ ДЛЯ ВСЕХ СЛОВ


    #f_init = open('monosyllabic_onsets_russian_lexemes.tsv', 'w')
    #f_init.write('monosyllabic_onsets_russian_lexemes' + '\n')

    #f_fin = open('monosyllabic_codas_russian_lexemes.tsv', 'w')
    #f_fin.write('monosyllabic_codas_russian_lexemes' + '\n')


    #f_init = open('monosyllabic_onsets_russian_wordforms.tsv', 'w')
    #f_init.write('monosyllabic_onsets_russian_wordforms' + '\n')

    #f_fin = open('monosyllabic_codas_russian_wordforms.tsv', 'w')
    #f_fin.write('monosyllabic_codas_russian_wordforms' + '\n')


    #f_init = open('monosyllabic_onsets_macedonian_lexemes.tsv', 'w')
    #f_init.write('monosyllabic_onsets_macedonian_lexemes' + '\n')

    #f_fin = open('monosyllabic_codas_macedonian_lexemes.tsv', 'w')
    #f_fin.write('monosyllabic_codas_macedonian_lexemes' + '\n')


    f_init = open('monosyllabic_onsets_polish_wordforms.tsv', 'w')
    f_init.write('monosyllabic_onsets_polish_wordforms' + '\n')

    f_fin = open('monosyllabic_codas_polish_wordforms.tsv', 'w')
    f_fin.write('monosyllabic_codas_polish_wordforms' + '\n')


    onset = 'V'
    coda = 'V'

    initials = []
    finals = []

    for line in f_lines:
        res_init = re.match('([^V]+?)(((-)*?[V])|$)', line)
        if res_init:
            onset = res_init.group(1)

        if onset not in initials:
            initials.append(onset)

            f_init.write(onset + '\n')

        res_fin = re.match('[V]*?-([^V]+?$)', line)
        if res_fin:
            coda = res_fin.group(1)

        if coda not in finals:
            finals.append(coda)

            f_fin.write(coda + '\n')

    f_init.close()
    f_fin.close()

# делает списки инициалей и финалей всех слов — потому что если вдруг для македонского будет мало, я возьму отсюда
def M_3():
    #f = open('ipa_lexemes_russian.tsv')
    #f = open('ipa_wordforms_russian.tsv')
    #f = open('ipa_lexemes_macedonian.tsv')
    f = open('ipa_wordforms_polish.tsv')

    f_lines = f.readlines()
    f_lines = f_lines[1:]  # РАБОЧАЯ ВЕРСИЯ ДЛЯ ВСЕХ СЛОВ

    #f_init = open('all_onsets_russian_lexemes.tsv', 'w')
    #f_init.write('all_onsets_russian_lexemes' + '\n')

    #f_fin = open('all_codas_russian_lexemes.tsv', 'w')
    #f_fin.write('all_codas_russian_lexemes' + '\n')


    #f_init = open('all_onsets_russian_wordforms.tsv', 'w')
    #f_init.write('all_onsets_russian_wordforms' + '\n')

    #f_fin = open('all_codas_russian_wordforms.tsv', 'w')
    #f_fin.write('all_codas_russian_wordforms' + '\n')


    #f_init = open('all_onsets_macedonian_lexemes.tsv', 'w')
    #f_init.write('all_onsets_macedonian_lexemes' + '\n')

    #f_fin = open('all_codas_macedonian_lexemes.tsv', 'w')
    #f_fin.write('all_codas_macedonian_lexemes' + '\n')


    f_init = open('all_onsets_polish_wordforms.tsv', 'w')
    f_init.write('all_onsets_polish_wordforms' + '\n')

    f_fin = open('all_codas_polish_wordforms.tsv', 'w')
    f_fin.write('all_codas_polish_wordforms' + '\n')

    onset = 'V'
    coda = 'V'

    initials = []
    finals = []

    for line in f_lines:
        res_init = re.match('([^V]+?)(((-)*?[V])|$)', line)
        if res_init:
            onset = res_init.group(1)

        if onset not in initials:
            initials.append(onset)

            f_init.write(onset + '\n')

        res_fin = re.match('[V]*?-([^V]+?$)', line)
        if res_fin:
            coda = res_fin.group(1)

        if coda not in finals:
            finals.append(coda)

            f_fin.write(coda + '\n')

    f_init.close()
    f_fin.close()

    return initials, finals

# делает таблицу общую
def M_4():
    #f = open('ipa_lexemes_russian.tsv')
    #f = open('ipa_wordforms_russian.tsv')
    #f = open('ipa_lexemes_macedonian.tsv')
    f = open('ipa_wordforms_polish.tsv')

    f_lines = f.readlines()
    f_lines = f_lines[1:]  # РАБОЧАЯ ВЕРСИЯ ДЛЯ ВСЕХ СЛОВ

    #f_bt = open('big_table_lexemes_russian.tsv', 'w')
    #f_bt.write('lexeme_russian' + '\t' + 'number_syllables' + '\t' + 'onset' + '\t' + 'coda' + '\n')

    #f_bt = open('big_table_wordforms_russian.tsv', 'w')
    #f_bt.write('wordforms_russian' + '\t' + 'number_syllables' + '\t' + 'onset' + '\t' + 'coda' + '\n')

    #f_bt = open('big_table_lexemes_macedonian.tsv', 'w')
    #f_bt.write('lexeme_macedonian' + '\t' + 'number_syllables' + '\t' + 'onset' + '\t' + 'coda' + '\n')

    f_bt = open('big_table_wordforms_polish.tsv', 'w')
    f_bt.write('wordforms_polish' + '\t' + 'number_syllables' + '\t' + 'onset' + '\t' + 'coda' + '\n')

    initials = []
    finals = []

    for line in f_lines:
        i= 0
        onset = 'V'
        coda = 'V'

        #print(line)
        #res_init = re.match('([^V]+?)(((-)*?[V])|$)', line)
        res_init = re.search('^([^V]+?)(((-)*?[V])|$)', line)
        if res_init:
            onset = res_init.group(1)

        if onset not in initials:
            initials.append(onset)

            #print(line, 'это было слово', onset)

        #print(line)
        res_fin = re.search('[V]*?-([^V]+?$)', line)
        if res_fin:
            coda = res_fin.group(1)

        if coda not in finals:
            finals.append(coda)

            #print(coda)

        for elem in line:
            if elem == 'V':
                i += 1

        word = line.strip()
        word = re.sub('\n', '', word)
        #print('word: ', word)

        f_bt.write(word + '\t' + str(i) + '\t' + onset + '\t' + coda + '\n')

    f_bt.close()

    # теперь посчитаем частотность

# запись в словарь
def F_w_d(my_dict, my_key):
    if my_key not in my_dict:
        my_dict[my_key] = 1
    else:
        my_dict[my_key] += 1

    return my_dict

# запись в файл
def F_write_in_file(data , f_name):
    f = open(f_name, 'w')
    f.write(data)
    #print(data)
    f.close()

# сортирует словарь и пишет файл
def F_sort_wd_items(my_items, items_name):
    sorted_items = sorted(my_items.items(), key=operator.itemgetter(1), reverse=True)
    items_freq = items_name + '\t' + 'frequency'
    for k in sorted_items:
        items_freq = items_freq + '\n' + k[0] + '\t' + str(k[1])
    f_name = 'frequency_' + items_name + '.tsv'
    F_write_in_file(items_freq, f_name)

# частотность последовательностей
def M_5():

    onsets_list = []
    finals_list = []

    onsets_dict = {}
    codas_dict = {}

    #f_tt = open('big_table_lexemes_russian.tsv')
    #f_tt = open('big_table_wordforms_russian.tsv')
    #f_tt = open('big_table_lexemes_macedonian.tsv')
    f_tt = open('big_table_wordforms_polish.tsv')

    f_lis = f_tt.readlines()
    f_lis = f_lis[1:]
    #print(f_lis)

    for line in f_lis:
        line = re.sub('\n', '', line)
        line = line.split('\t')

        #print(line)

        onsets_list.append(line[2])
        finals_list.append(line[3])

        onsets_dict = F_w_d(onsets_dict, line[2])
        codas_dict = F_w_d(codas_dict, line[3])

    #print(onsets_dict)
    #print(codas_dict)

    #F_sort_wd_items(onsets_dict, 'onset_russian_lexemes')
    #F_sort_wd_items(codas_dict, 'coda_russian_lexemes')

    #F_sort_wd_items(onsets_dict, 'onset_russian_wordforms')
    #F_sort_wd_items(codas_dict, 'coda_russian_wordforms')

    #F_sort_wd_items(onsets_dict, 'onset_macedonian_lexemes')
    #F_sort_wd_items(codas_dict, 'coda_macedonian_lexemes')

    F_sort_wd_items(onsets_dict, 'onset_polish_wordforms')
    F_sort_wd_items(codas_dict, 'coda_polish_wordforms')


#M_1()

#M_2()

#M_3()

#M_4()

M_5()

print("--- %s seconds ---" % (time.time() - start_time))