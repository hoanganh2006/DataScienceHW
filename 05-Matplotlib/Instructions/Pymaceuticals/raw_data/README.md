

```python
#Dependencies
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
%matplotlib inline
```


```python
#Read the first csv file clinicaltrial_data.csv and convert that into dataframe
clinical = ('clinicaltrial_data.csv')
clinical = pd.read_csv(clinical)
clinical_df = pd.DataFrame(clinical)
clinical_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mouse ID</th>
      <th>Timepoint</th>
      <th>Tumor Volume (mm3)</th>
      <th>Metastatic Sites</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b128</td>
      <td>0</td>
      <td>45.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>f932</td>
      <td>0</td>
      <td>45.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>g107</td>
      <td>0</td>
      <td>45.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a457</td>
      <td>0</td>
      <td>45.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>c819</td>
      <td>0</td>
      <td>45.0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Read the second csv file mouse_drug_data.csv and convert that into dataframe
mouse_drug = ('mouse_drug_data.csv')
mouse_drug = pd.read_csv(mouse_drug)
mouse_drug_df = pd.DataFrame(mouse_drug)
mouse_drug_df = mouse_drug_df.sort_values('Drug')
drug_test = pd.merge(clinical_df, mouse_drug_df, on = "Mouse ID", how = 'outer')
drug_test.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mouse ID</th>
      <th>Timepoint</th>
      <th>Tumor Volume (mm3)</th>
      <th>Metastatic Sites</th>
      <th>Drug</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b128</td>
      <td>0</td>
      <td>45.000000</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b128</td>
      <td>5</td>
      <td>45.651331</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b128</td>
      <td>10</td>
      <td>43.270852</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b128</td>
      <td>15</td>
      <td>43.784893</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>4</th>
      <td>b128</td>
      <td>20</td>
      <td>42.731552</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
  </tbody>
</table>
</div>




```python
drug_test_1 = drug_test.drop(columns = ['Mouse ID','Metastatic Sites'])
drug_test_1 = drug_test_1.groupby(['Drug', 'Timepoint'])['Tumor Volume (mm3)'].mean()
drug_test_df = pd.DataFrame(drug_test_1)
drug_df = drug_test_df.unstack(level = 0)
drug_df.columns = drug_df.columns.droplevel()
drug_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Drug</th>
      <th>Capomulin</th>
      <th>Ceftamin</th>
      <th>Infubinol</th>
      <th>Ketapril</th>
      <th>Naftisol</th>
      <th>Placebo</th>
      <th>Propriva</th>
      <th>Ramicane</th>
      <th>Stelasyn</th>
      <th>Zoniferol</th>
    </tr>
    <tr>
      <th>Timepoint</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>44.266086</td>
      <td>46.503051</td>
      <td>47.062001</td>
      <td>47.389175</td>
      <td>46.796098</td>
      <td>47.125589</td>
      <td>47.248967</td>
      <td>43.944859</td>
      <td>47.527452</td>
      <td>46.851818</td>
    </tr>
    <tr>
      <th>10</th>
      <td>43.084291</td>
      <td>48.285125</td>
      <td>49.403909</td>
      <td>49.582269</td>
      <td>48.694210</td>
      <td>49.423329</td>
      <td>49.101541</td>
      <td>42.531957</td>
      <td>49.463844</td>
      <td>48.689881</td>
    </tr>
    <tr>
      <th>15</th>
      <td>42.064317</td>
      <td>50.094055</td>
      <td>51.296397</td>
      <td>52.399974</td>
      <td>50.933018</td>
      <td>51.359742</td>
      <td>51.067318</td>
      <td>41.495061</td>
      <td>51.529409</td>
      <td>50.779059</td>
    </tr>
    <tr>
      <th>20</th>
      <td>40.716325</td>
      <td>52.157049</td>
      <td>53.197691</td>
      <td>54.920935</td>
      <td>53.644087</td>
      <td>54.364417</td>
      <td>53.346737</td>
      <td>40.238325</td>
      <td>54.067395</td>
      <td>53.170334</td>
    </tr>
  </tbody>
</table>
</div>




```python
x_axis = list(range(0, 50, 5))
```


```python
for drug in drug_df.columns: 
    plt.plot(x_axis, drug_df[drug], marker = "d", markeredgecolor = "black", linestyle = 'dashed', label = drug)
plt.title("Tumor Response to Treatment")
plt.xlabel("Time (Days)")
plt.ylabel("Tumor Volume (mm3)")
plt.ylim(20, 80)
plt.xlim(0, 45, 5)
plt.grid(color='black', linestyle='--', linewidth=0.5)
plt.legend(["Capomulin", "Ceftamin", "Infubinol", "Ketapril"])
plt.savefig('Tumor_Response_to_Treatment.png')
#need to add error bar within it
```


![png](output_5_0.png)



```python
drug_meta = drug_test.drop(columns = ['Mouse ID','Tumor Volume (mm3)'])
drug_meta = drug_meta.groupby(['Drug', 'Timepoint'])['Metastatic Sites'].mean()
drug_meta = pd.DataFrame(drug_meta)
drug_meta_df = drug_meta.unstack(level = 0)
drug_meta_df.columns = drug_meta_df.columns.droplevel()
drug_meta_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Drug</th>
      <th>Capomulin</th>
      <th>Ceftamin</th>
      <th>Infubinol</th>
      <th>Ketapril</th>
      <th>Naftisol</th>
      <th>Placebo</th>
      <th>Propriva</th>
      <th>Ramicane</th>
      <th>Stelasyn</th>
      <th>Zoniferol</th>
    </tr>
    <tr>
      <th>Timepoint</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.160000</td>
      <td>0.380952</td>
      <td>0.280000</td>
      <td>0.304348</td>
      <td>0.260870</td>
      <td>0.375000</td>
      <td>0.320000</td>
      <td>0.120000</td>
      <td>0.240000</td>
      <td>0.166667</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.320000</td>
      <td>0.600000</td>
      <td>0.666667</td>
      <td>0.590909</td>
      <td>0.523810</td>
      <td>0.833333</td>
      <td>0.565217</td>
      <td>0.250000</td>
      <td>0.478261</td>
      <td>0.500000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.375000</td>
      <td>0.789474</td>
      <td>0.904762</td>
      <td>0.842105</td>
      <td>0.857143</td>
      <td>1.250000</td>
      <td>0.764706</td>
      <td>0.333333</td>
      <td>0.782609</td>
      <td>0.809524</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0.652174</td>
      <td>1.111111</td>
      <td>1.050000</td>
      <td>1.210526</td>
      <td>1.150000</td>
      <td>1.526316</td>
      <td>1.000000</td>
      <td>0.347826</td>
      <td>0.952381</td>
      <td>1.294118</td>
    </tr>
  </tbody>
</table>
</div>




```python
for drug in drug_meta_df.columns: 
    plt.plot(x_axis, drug_meta_df[drug], marker = "s",markeredgecolor = "black", linestyle = 'dashed', label = drug)
plt.title("Metastatic Spread During Treatment")
plt.xlabel("Time (Days)")
plt.ylabel("Met. Sites")
plt.ylim(0.0, 4.0, 0.5)
plt.xlim(0, 45, 5)
plt.grid(color='black', linestyle='--', linewidth=0.5)
plt.legend(["Capomulin", "Ceftamin", "Infubinol", "Ketapril"])
plt.savefig('Metastatic_Spread_During_Treatment.png')
#need to add error bar within it
```


![png](output_7_0.png)



```python
drug_survive = drug_test.drop(columns = ['Tumor Volume (mm3)','Metastatic Sites'])
drug_survive = drug_survive.groupby(['Drug', 'Timepoint'])['Mouse ID'].count()
drug_survive_df = pd.DataFrame(drug_survive)
survive_df = drug_survive_df.unstack(level = 0)
survive_df.columns = survive_df.columns.droplevel()
survive_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Drug</th>
      <th>Capomulin</th>
      <th>Ceftamin</th>
      <th>Infubinol</th>
      <th>Ketapril</th>
      <th>Naftisol</th>
      <th>Placebo</th>
      <th>Propriva</th>
      <th>Ramicane</th>
      <th>Stelasyn</th>
      <th>Zoniferol</th>
    </tr>
    <tr>
      <th>Timepoint</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25</td>
      <td>25</td>
      <td>25</td>
      <td>25</td>
      <td>25</td>
      <td>25</td>
      <td>26</td>
      <td>25</td>
      <td>26</td>
      <td>25</td>
    </tr>
    <tr>
      <th>5</th>
      <td>25</td>
      <td>21</td>
      <td>25</td>
      <td>23</td>
      <td>23</td>
      <td>24</td>
      <td>25</td>
      <td>25</td>
      <td>25</td>
      <td>24</td>
    </tr>
    <tr>
      <th>10</th>
      <td>25</td>
      <td>20</td>
      <td>21</td>
      <td>22</td>
      <td>21</td>
      <td>24</td>
      <td>23</td>
      <td>24</td>
      <td>23</td>
      <td>22</td>
    </tr>
    <tr>
      <th>15</th>
      <td>24</td>
      <td>19</td>
      <td>21</td>
      <td>19</td>
      <td>21</td>
      <td>20</td>
      <td>17</td>
      <td>24</td>
      <td>23</td>
      <td>21</td>
    </tr>
    <tr>
      <th>20</th>
      <td>23</td>
      <td>18</td>
      <td>20</td>
      <td>19</td>
      <td>20</td>
      <td>19</td>
      <td>17</td>
      <td>23</td>
      <td>21</td>
      <td>17</td>
    </tr>
  </tbody>
</table>
</div>




```python
for drug in survive_df.columns: 
    plt.plot(x_axis, (survive_df[drug]/survive_df[drug][0])*100, marker = "o",markeredgecolor = "black", linestyle = 'dashed', label = drug)
plt.title("Survival During Treatment")
plt.xlabel("Time (Days)")
plt.ylabel("Survival Rate (%)")
plt.ylim(40, 100, 10)
plt.xlim(0, 45, 5)
plt.grid(color='black', linestyle='--', linewidth=0.5)
plt.legend(["Capomulin", "Ceftamin", "Infubinol", "Ketapril"], loc = 'best')
plt.savefig('Survival_During_Treatment.png')
```


![png](output_9_0.png)



```python
total_change = pd.DataFrame()
drug_name = []
change = []
for drug in drug_df.columns: 
    percentage_change = ((drug_df[drug][0] - drug_df[drug][45])/drug_df[drug][0])*100
    change.append(percentage_change)
    drug_name.append(drug)
total_change['Total % Tumor Volume Change'] = change
total_change['Drug'] = drug_name
total_change = total_change[['Drug', 'Total % Tumor Volume Change']]
total_change
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Drug</th>
      <th>Total % Tumor Volume Change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Capomulin</td>
      <td>19.475303</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ceftamin</td>
      <td>-42.516492</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Infubinol</td>
      <td>-46.123472</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ketapril</td>
      <td>-57.028795</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Naftisol</td>
      <td>-53.923347</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Placebo</td>
      <td>-51.297960</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Propriva</td>
      <td>-47.241175</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Ramicane</td>
      <td>22.320900</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Stelasyn</td>
      <td>-52.085134</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Zoniferol</td>
      <td>-46.579751</td>
    </tr>
  </tbody>
</table>
</div>




```python
negative = []
positive = []
drug_pos = []
drug_neg = []
for row_value, row in total_change.iterrows():
    if row[1] > 0: 
        positive.append(row[1])
        drug_pos.append(row[0])
    else: 
        negative.append(row[1])
        drug_neg.append(row[0])
```


```python
x_axis_pos = np.arange(len(positive))
x_axis_neg = np.arange(len(negative))
tick_locations_pos = [i + 0.4 for i in x_axis_pos]
plt.xticks(tick_locations_pos, drug_pos, rotation = '45')
plt.bar(x_axis_pos, positive, color='r', alpha=0.5, align="edge", edgecolor = "black")
tick_locations_neg = [i + 0.4 for i in x_axis_neg]
plt.xticks(tick_locations_neg, drug_neg, rotation = '45')
plt.bar(x_axis_neg, negative, color='g', alpha=0.5, align="edge", edgecolor = "black")
plt.title("Tumor Change Over 45 Day Treatment")
plt.ylabel("% Tumor Volume Change") 
plt.grid(color='black', linestyle='--', linewidth=0.5)
plt.savefig("Tumor_Change_Over_45_Day_Treatment.png")
```


![png](output_12_0.png)

