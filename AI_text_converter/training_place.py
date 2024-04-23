# import matplotlib.pyplot as plt
# from datetime import datetime,timedelta
#
# # Dane
# dates = ['2024-04-01', '2024-04-02', '2024-04-03']
# start_times = [8, 9, 10]
# end_times = [16, 17, 18]
#
# # Konwersja łańcuchów dat na obiekty datetime
# dates = [datetime.strptime(date, '%Y-%m-%d') for date in dates]
#
# # Szerokość słupków
# bar_width_start = 0.10
# bar_width_end = 0.35
#
# # Tworzenie wykresu słupkowego
#
# plt.bar(dates, end_times, width=bar_width_end, label='End Time')  # Przesunięcie słupków o bar_width
# plt.bar(dates, start_times, width=bar_width_start, label='Start Time')
# # Ustawienie etykiet i tytułu
# plt.xlabel('Date')
# plt.ylabel('Time')
# plt.title('Event Timeline')
# plt.xticks(dates, [date.strftime('%Y-%m-%d') for date in dates])  # Ustawienie etykiet osi x w formacie daty
# plt.legend()
#
# # Wyświetlenie wykresu
# plt.show()
