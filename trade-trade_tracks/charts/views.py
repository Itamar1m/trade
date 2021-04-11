from django.shortcuts import render,redirect
from daily_tracker.models import *
import plotly.graph_objects as go 
import pandas as pd 
import requests
import finplot as fplt
import numpy as np
import plotly.express as px


def chart(request):
    return render(request,'chart.html')


def daily_chart(request,stock,date,pk):

    chart_time=request.GET.get('chart_time_frame_in_minutes')
    api_key='pp9Bo8dAXHWwaUcqYimJqf1x5doWrqED'
    table =UserCustomTable.objects.get(pk=pk)
    symbol = stock.upper()
    date = date
   

    result=requests.get(f'https://api.polygon.io/v2/aggs/ticker/{symbol}/range/{chart_time}/minute/{date}/{date}?unadjusted=true&sort=asc&limit=5000&apiKey={api_key}')
    data=result.json()
    fplot=pd.DataFrame(data['results'])
    fplot=fplot.rename(columns={'t':'time','o':'open', 'c':'close', 'h':'high', 'l':'low','v':'volume'})
    figure = go.Figure(
    data =[
        go.Candlestick(
            x=fplot['time'],
            low=fplot['low'],
            high=fplot['high'],
            close=fplot['close'],
            open=fplot['open'],
            increasing_line_color='#16B222',
            decreasing_line_color='red'
        )])
    figure.update_layout(
    title={
        'text':f'{stock.upper()}  {date} | {chart_time} minute chart'})
    figure.write_html("view-table",table.pk)
    # graph_div = fplot.offline.plot(figure, auto_open = False, output_type="div")
    figure.show()
    # ax = fplt.create_plot(f'{stock.upper()} - {date} 5 minute chart', rows=1)

    # candles = fplot[['time','open','close','high','low']]
    # fplt.candlestick_ochl(candles, ax=ax)

    # volumes = fplot[['time','open','close','volume']]
    # fplt.volume_ocv(volumes, ax=ax.overlay())
    # fplt.autoviewrestore()
    # # def save():
    # #     fplt.screenshot(open('screenshot.png', 'wb'))
    # #     fplt.timer_callback(save, 0.5, single_shot=True) 
    # # save()
    # chart = fplt.show()

    return redirect('view-table',table.pk)    