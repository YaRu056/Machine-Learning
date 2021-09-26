# Machine-Learning

## 一、	 資料集合一 (final_project_dataset_1.csv)
![image](https://user-images.githubusercontent.com/82867224/134674194-00a9d192-84ec-4e56-8c87-2a4c2c7cc819.png)
###### Figure 1年紀、性別與保險費之間的關係圖
保險費在20000以下會隨著年齡的增長而增加，性別對保險費沒有明顯差異。

![image](https://user-images.githubusercontent.com/82867224/134674487-6c22e743-6108-4679-a7d7-36e215fa4e51.png)
###### Figure 2 BMI、吸菸與保險費之間的關係圖
BMI對保險費的影響沒有吸菸與否那麼重要，若有吸菸且BMI>=30時，保險費從30000起跳。

![image](https://user-images.githubusercontent.com/82867224/134674552-a33b9478-0fab-447d-b17f-c384c5cf33e4.png)
###### Figure 3 地區、性別與保險費之間的關係圖
東南部地區的保險費比其他三地區來的高，將地區歸類為是否來自東南地區。

![image](https://user-images.githubusercontent.com/82867224/134674599-0d3c60d9-7f94-43df-95e7-020a2fb5f6bd.png)
###### Figure 4 子女數量、吸菸與保險費之間的關係圖
不論子女數量的多少，吸菸者的保險費通常從15000起跳，非吸菸者通常最高保險費不高於20000。

![image](https://user-images.githubusercontent.com/82867224/134674650-d0cfe6e5-4ef6-48e9-a796-637101714f7b.png)

###### Figure 5 特徵之間的關聯圖

不同特徵之間沒有高度的相關性。

* 前處理分析:
吸菸與否對此模型很重要，保險費和性別與子女數量較無相關，將地區畫分是否為東南部，避免有過多的參數導致過度學習。

* 模型:
反向淘汰
藉由反向淘汰去計算每一個自變數的P值，來顯示自變數對模型有多大的影響力。

* 結論: 
* ![image](https://user-images.githubusercontent.com/82867224/134674845-7d675e61-23f5-4392-8775-a573acff60e2.png)
###### Figure 6 剩餘費用和實際費用
最後的R-squared為0.734，呈現中度相關性，在上圖剩餘費用和實際費用的圖表中，可以發現在15000內的保線費預測誤差較小。


## 二、資料集合 二 (final_project_dataset_2.csv)

* 前處理分析:

  1. 由於 我們 認為 有 缺失 值 的 資料 可能 會影響資料分析，所以我們先將有缺
  失資料的行刪除以免影響模型。
  2. 我們認為日期、地點 、風向 都不是影響明日是否會下雨的因素，因此將'Date','Location','WindGustDir', 'WindDir9am', 'WindDir3pm'刪除。
  3. 之後 我們將 'RainToday','RainTomorrow' 進行標籤編碼。
  4. 之後將資料切割訓練集與測試集， 先實驗 test_size=0.25,random_state=0

* 模型:

  我們嘗試使用下列三個模型來進行預測分類 :
  
  1. SVM:算完後正確率達 85.8%
  2. RandomForest: 算完後正確率達 85.5%
  3. SVM kernal: 算完後正確率達 84.3%
 
  之後我們嘗試調整訓練集的 test_size和 random_state的值，不過算出的正確率並沒有差別太大。所以還是用 test_size=0.25,random_state=0下去算。
  算完之後的結論我們發現，SVM算完的結果更高 遂 使用 SVM預測 。
