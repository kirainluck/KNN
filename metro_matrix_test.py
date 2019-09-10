"""
Created on Mon Sep 9  
@author: Pavel
"""

# v1 Расстоянием считаем число станций от начальной до конечной.
# Станции пересадки считаем за одну.
# Источник https://yandex.ru/metro/moscow

METRO = {
    "академическая": {"академическая": 0, "царицыно": 11, "окружная": 13, "тимирязевская": 11,
                      "молодежная": 9, "текстильщики": 8, "войковская": 12, "бабушкинская": 14, "отрадное": 14,
                      "орехово": 12, "ховрино": 16, "бутырская": 10, "комсомольская": 8,
                      "речной вокзал": 14, "сокол": 11, },
    "царицыно":      {"академическая": 11, "царицыно": 0, "окружная": 16, "тимирязевская": 14,
                      "молодежная": 14, "текстильщики": 10,"войковская": 15, "бабушкинская": 17, "отрадное": 17,
                      "орехово": 1, "ховрино": 19, "бутырская": 13, "комсомольская": 12,
                      "речной вокзал": 17, "сокол": 14, },
    "окружная":      {"академическая": 13, "царицыно": 16, "окружная": 0,"тимирязевская": 2,
                      "молодежная": 13, "текстильщики": 13,"войковская": 10, "бабушкинская": 5, "отрадное": 3,
                      "орехово": 17, "ховрино": 14, "бутырская": 3, "комсомольская": 9,
                      "речной вокзал": 12, "сокол": 9, },
                      
                      
                      
    "тимирязевская": {"академическая": 11, "царицыно": 14, "окружная": 2,"тимирязевская": 0,
                      "молодежная": 9, "текстильщики": 11, "войковская": 8, "бабушкинская": 5, "отрадное": 3,
                      "орехово": 15, "ховрино": 12, "бутырская": 3, "комсомольская": 5,
                      "речной вокзал": 10, "сокол": 7, },
    "молодежная":     {"академическая": 9, "царицыно": 14, "окружная": 13,"тимирязевская": 9,
                      "молодежная": 0, "текстильщики": 12, "войковская": 10, "бабушкинская": 14, "отрадное": 15,
                      "орехово": 15, "ховрино": 14, "бутырская": 11, "комсомольская": 11,
                      "речной вокзал": 12, "сокол": 9, },
    "текстильщики":      {"академическая": 8, "царицыно": 10, "окружная": 13,"тимирязевская": 11,
                      "молодежная": 12, "текстильщики": 0,"войковская": 12, "бабушкинская": 13, "отрадное": 14,
                      "орехово": 11, "ховрино": 16, "бутырская": 9, "комсомольская": 8,
                      "речной вокзал": 14, "сокол": 11, },
    "войковская":      {"академическая": 12, "царицыно": 15, "окружная": 10,"тимирязевская": 8,
                      "молодежная": 10, "текстильщики": 12,"войковская": 0, "бабушкинская": 12, "отрадное": 11,
                      "орехово": 16, "ховрино": 4, "бутырская": 10, "комсомольская": 11,
                      "речной вокзал": 2, "сокол": 1, },
    "бабушкинская":      {"академическая": 14, "царицыно": 17, "окружная": 5,"тимирязевская": 5,
                      "молодежная": 14, "текстильщики": 13,"войковская": 12, "бабушкинская": 0, "отрадное": 4,
                      "орехово": 18, "ховрино": 16, "бутырская": 12, "комсомольская": 10,
                      "речной вокзал": 14, "сокол": 11, },
    "отрадное":      {"академическая": 14, "царицыно": 17, "окружная": 3,"тимирязевская": 3,
                      "молодежная": 15, "текстильщики": 14,"войковская": 11, "бабушкинская": 4, "отрадное": 0,
                      "орехово": 18, "ховрино": 15, "бутырская": 4, "комсомольская": 8,
                      "речной вокзал": 13, "сокол": 10, },
    "орехово":      {"академическая": 12, "царицыно": 1, "окружная": 17,"тимирязевская": 15,
                      "молодежная": 15, "текстильщики": 11,"войковская": 16, "бабушкинская": 18, "отрадное": 18,
                      "орехово": 0, "ховрино": 20, "бутырская": 14, "комсомольская": 13,
                      "речной вокзал": 18, "сокол": 15, },
    "ховрино":      {"академическая": 16, "царицыно": 19, "окружная": 14,"тимирязевская": 12,
                      "молодежная": 14, "текстильщики": 16,"войковская": 4, "бабушкинская": 16, "отрадное": 15,
                      "орехово": 20, "ховрино": 0, "бутырская": 14, "комсомольская": 15,
                      "речной вокзал": 2, "сокол": 5, },
    "бутырская":      {"академическая": 10, "царицыно": 13, "окружная": 3,"тимирязевская": 3,
                      "молодежная": 11, "текстильщики": 9,"войковская": 10, "бабушкинская": 12, "отрадное": 4,
                      "орехово": 14, "ховрино": 14, "бутырская": 0, "комсомольская": 6,
                      "речной вокзал": 12, "сокол": 9, },
    "комсомольская":      {"академическая": 8, "царицыно": 12, "окружная": 9,"тимирязевская": 5,
                      "молодежная": 11, "текстильщики": 8,"войковская": 11, "бабушкинская": 10, "отрадное": 8,
                      "орехово": 13, "ховрино": 15, "бутырская": 6, "комсомольская": 0,
                      "речной вокзал": 13, "сокол": 10, },
    "речной вокзал":      {"академическая": 14, "царицыно": 17, "окружная": 12,"тимирязевская": 10,
                      "молодежная": 12, "текстильщики": 14,"войковская": 2, "бабушкинская": 14, "отрадное": 13,
                      "орехово": 18, "ховрино": 2, "бутырская": 12, "комсомольская": 13,
                      "речной вокзал": 0, "сокол": 3, },
    "сокол":      {"академическая": 11, "царицыно": 12, "окружная": 9,"тимирязевская": 7,
                      "молодежная": 9, "текстильщики": 11,"войковская": 1, "бабушкинская": 11, "отрадное": 10,
                      "орехово": 15, "ховрино": 5, "бутырская": 9, "комсомольская": 10,
                      "речной вокзал": 3, "сокол": 0, },
                
}
