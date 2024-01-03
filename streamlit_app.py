import pandas as pd
import numpy as np
import streamlit as st

def simulate(n_simulation, initial_asset, yearly_repayment,r_mean, r_std):
    asset_lists = []
    for _ in range(n_simulation):
        asset_list = []
        asset_current = initial_asset
        asset_list.append(asset_current)

        for _ in range(19):
            # 年利(r)を正規分布からサンプリング
            r = np.random.normal(r_mean, r_std)

            # 次の期の asset を計算
            asset_next = (1 + r) * (asset_current - yearly_repayment)

            # 結果をリストに追加
            asset_list.append(asset_next)

            # asset_currentを更新
            asset_current = asset_next

        asset_lists.append(asset_list)
    return asset_lists

def visualize_result(asset_lists, start_year):
    asset_lists = np.array(asset_lists)
    date_range = [year for year in range(start_year, start_year + asset_lists.shape[1])]
    df = pd.DataFrame(asset_lists.T)
    df['年'] = date_range

    st.write("### あなたの資産推移")
    st.line_chart(df, x='年')

    


if __name__ == '__main__':
    st.write('## 奨学金 資産運用 シュミレーション')
    st.write('あなたは大学卒業と同時に株式投資を始めます．\
            卒業時の資産をすべて株式に投資をし，その資産を切り崩しながら奨学金の返済を行うものとします．\
            このときのあなたの資産額推移をモンテカルロ・シミュレーションします．\
            あなたの投資パフォーマンス（年間リターン）は正規分布$N(\mu, \sigma^2)$ に従うと仮定します．')


    st.sidebar.write('## 奨学金貸与情報の入力')
    total_amount = st.sidebar.number_input('総貸与額 (万円)', min_value=1,value=500, step=1) * 10**4    
    r = st.sidebar.number_input('貸与利率(%)',  min_value=0.001, max_value=3.0, step=0.001)

    yearly_repayment = r * (1+r)**20 * total_amount / ((1+r)**20 - 1)

    start_year = st.sidebar.number_input('返還開始年', min_value=1900, max_value=2100, value=2027, step=1)

    st.sidebar.caption(f'あなたは毎月{int(yearly_repayment//12):,}円，20年間返済します．')
    st.sidebar.divider()


    st.sidebar.write('## 資産額を入力')
    initial_asset = st.sidebar.number_input('卒業時の資産額 (万円)', min_value=1,value=500, step=1) * 10**4
    st.sidebar.divider()


    st.sidebar.write('## 投資パフォーマンスの入力')
    st.sidebar.write('デフォルトの値はバンガード S&P500 ETF (VOO)の過去10年間のデータをもとに算出   ')
    mu = st.sidebar.number_input('リターンの平均(％)', value=11.0) / 100
    sigma = st.sidebar.number_input('リターン標準偏差(％)',value=12.0) / 100
    st.sidebar.divider()



    n_simulation = st.sidebar.slider('シミュレーション回数', min_value=1, max_value=20, value=10, step=1)
    if st.sidebar.button('シミュレーション開始'):
        asset_lists = simulate(n_simulation, initial_asset, yearly_repayment, r_mean=mu, r_std=sigma)
        visualize_result(asset_lists, start_year)

