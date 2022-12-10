```python
import pandas as pd
```


```python
df = pd.read_csv('C:\\Users\\Public\\dataset\\train.csv')
```


```python
df.head()
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
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.tail()
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
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>886</th>
      <td>887</td>
      <td>0</td>
      <td>2</td>
      <td>Montvila, Rev. Juozas</td>
      <td>male</td>
      <td>27.0</td>
      <td>0</td>
      <td>0</td>
      <td>211536</td>
      <td>13.00</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>887</th>
      <td>888</td>
      <td>1</td>
      <td>1</td>
      <td>Graham, Miss. Margaret Edith</td>
      <td>female</td>
      <td>19.0</td>
      <td>0</td>
      <td>0</td>
      <td>112053</td>
      <td>30.00</td>
      <td>B42</td>
      <td>S</td>
    </tr>
    <tr>
      <th>888</th>
      <td>889</td>
      <td>0</td>
      <td>3</td>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
      <td>female</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>W./C. 6607</td>
      <td>23.45</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>889</th>
      <td>890</td>
      <td>1</td>
      <td>1</td>
      <td>Behr, Mr. Karl Howell</td>
      <td>male</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>111369</td>
      <td>30.00</td>
      <td>C148</td>
      <td>C</td>
    </tr>
    <tr>
      <th>890</th>
      <td>891</td>
      <td>0</td>
      <td>3</td>
      <td>Dooley, Mr. Patrick</td>
      <td>male</td>
      <td>32.0</td>
      <td>0</td>
      <td>0</td>
      <td>370376</td>
      <td>7.75</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[15:31]
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
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>1</td>
      <td>2</td>
      <td>Hewlett, Mrs. (Mary D Kingcome)</td>
      <td>female</td>
      <td>55.0</td>
      <td>0</td>
      <td>0</td>
      <td>248706</td>
      <td>16.0000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>0</td>
      <td>3</td>
      <td>Rice, Master. Eugene</td>
      <td>male</td>
      <td>2.0</td>
      <td>4</td>
      <td>1</td>
      <td>382652</td>
      <td>29.1250</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>1</td>
      <td>2</td>
      <td>Williams, Mr. Charles Eugene</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>244373</td>
      <td>13.0000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>0</td>
      <td>3</td>
      <td>Vander Planke, Mrs. Julius (Emelia Maria Vande...</td>
      <td>female</td>
      <td>31.0</td>
      <td>1</td>
      <td>0</td>
      <td>345763</td>
      <td>18.0000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>1</td>
      <td>3</td>
      <td>Masselmani, Mrs. Fatima</td>
      <td>female</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>2649</td>
      <td>7.2250</td>
      <td>NaN</td>
      <td>C</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>0</td>
      <td>2</td>
      <td>Fynney, Mr. Joseph J</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>239865</td>
      <td>26.0000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
      <td>1</td>
      <td>2</td>
      <td>Beesley, Mr. Lawrence</td>
      <td>male</td>
      <td>34.0</td>
      <td>0</td>
      <td>0</td>
      <td>248698</td>
      <td>13.0000</td>
      <td>D56</td>
      <td>S</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
      <td>1</td>
      <td>3</td>
      <td>McGowan, Miss. Anna "Annie"</td>
      <td>female</td>
      <td>15.0</td>
      <td>0</td>
      <td>0</td>
      <td>330923</td>
      <td>8.0292</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24</td>
      <td>1</td>
      <td>1</td>
      <td>Sloper, Mr. William Thompson</td>
      <td>male</td>
      <td>28.0</td>
      <td>0</td>
      <td>0</td>
      <td>113788</td>
      <td>35.5000</td>
      <td>A6</td>
      <td>S</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25</td>
      <td>0</td>
      <td>3</td>
      <td>Palsson, Miss. Torborg Danira</td>
      <td>female</td>
      <td>8.0</td>
      <td>3</td>
      <td>1</td>
      <td>349909</td>
      <td>21.0750</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>25</th>
      <td>26</td>
      <td>1</td>
      <td>3</td>
      <td>Asplund, Mrs. Carl Oscar (Selma Augusta Emilia...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>5</td>
      <td>347077</td>
      <td>31.3875</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27</td>
      <td>0</td>
      <td>3</td>
      <td>Emir, Mr. Farred Chehab</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>2631</td>
      <td>7.2250</td>
      <td>NaN</td>
      <td>C</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
      <td>0</td>
      <td>1</td>
      <td>Fortune, Mr. Charles Alexander</td>
      <td>male</td>
      <td>19.0</td>
      <td>3</td>
      <td>2</td>
      <td>19950</td>
      <td>263.0000</td>
      <td>C23 C25 C27</td>
      <td>S</td>
    </tr>
    <tr>
      <th>28</th>
      <td>29</td>
      <td>1</td>
      <td>3</td>
      <td>O'Dwyer, Miss. Ellen "Nellie"</td>
      <td>female</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>330959</td>
      <td>7.8792</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>0</td>
      <td>3</td>
      <td>Todoroff, Mr. Lalio</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>349216</td>
      <td>7.8958</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>30</th>
      <td>31</td>
      <td>0</td>
      <td>1</td>
      <td>Uruchurtu, Don. Manuel E</td>
      <td>male</td>
      <td>40.0</td>
      <td>0</td>
      <td>0</td>
      <td>PC 17601</td>
      <td>27.7208</td>
      <td>NaN</td>
      <td>C</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[50:101:5]
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
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>50</th>
      <td>51</td>
      <td>0</td>
      <td>3</td>
      <td>Panula, Master. Juha Niilo</td>
      <td>male</td>
      <td>7.0</td>
      <td>4</td>
      <td>1</td>
      <td>3101295</td>
      <td>39.6875</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>55</th>
      <td>56</td>
      <td>1</td>
      <td>1</td>
      <td>Woolner, Mr. Hugh</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>19947</td>
      <td>35.5000</td>
      <td>C52</td>
      <td>S</td>
    </tr>
    <tr>
      <th>60</th>
      <td>61</td>
      <td>0</td>
      <td>3</td>
      <td>Sirayanian, Mr. Orsen</td>
      <td>male</td>
      <td>22.0</td>
      <td>0</td>
      <td>0</td>
      <td>2669</td>
      <td>7.2292</td>
      <td>NaN</td>
      <td>C</td>
    </tr>
    <tr>
      <th>65</th>
      <td>66</td>
      <td>1</td>
      <td>3</td>
      <td>Moubarek, Master. Gerios</td>
      <td>male</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2661</td>
      <td>15.2458</td>
      <td>NaN</td>
      <td>C</td>
    </tr>
    <tr>
      <th>70</th>
      <td>71</td>
      <td>0</td>
      <td>2</td>
      <td>Jenkin, Mr. Stephen Curnow</td>
      <td>male</td>
      <td>32.0</td>
      <td>0</td>
      <td>0</td>
      <td>C.A. 33111</td>
      <td>10.5000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>75</th>
      <td>76</td>
      <td>0</td>
      <td>3</td>
      <td>Moen, Mr. Sigurd Hansen</td>
      <td>male</td>
      <td>25.0</td>
      <td>0</td>
      <td>0</td>
      <td>348123</td>
      <td>7.6500</td>
      <td>F G73</td>
      <td>S</td>
    </tr>
    <tr>
      <th>80</th>
      <td>81</td>
      <td>0</td>
      <td>3</td>
      <td>Waelens, Mr. Achille</td>
      <td>male</td>
      <td>22.0</td>
      <td>0</td>
      <td>0</td>
      <td>345767</td>
      <td>9.0000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>85</th>
      <td>86</td>
      <td>1</td>
      <td>3</td>
      <td>Backstrom, Mrs. Karl Alfred (Maria Mathilda Gu...</td>
      <td>female</td>
      <td>33.0</td>
      <td>3</td>
      <td>0</td>
      <td>3101278</td>
      <td>15.8500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>90</th>
      <td>91</td>
      <td>0</td>
      <td>3</td>
      <td>Christmann, Mr. Emil</td>
      <td>male</td>
      <td>29.0</td>
      <td>0</td>
      <td>0</td>
      <td>343276</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>95</th>
      <td>96</td>
      <td>0</td>
      <td>3</td>
      <td>Shorney, Mr. Charles Joseph</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>374910</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>100</th>
      <td>101</td>
      <td>0</td>
      <td>3</td>
      <td>Petranec, Miss. Matilda</td>
      <td>female</td>
      <td>28.0</td>
      <td>0</td>
      <td>0</td>
      <td>349245</td>
      <td>7.8958</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.dtypes
```




    PassengerId      int64
    Survived         int64
    Pclass           int64
    Name            object
    Sex             object
    Age            float64
    SibSp            int64
    Parch            int64
    Ticket          object
    Fare           float64
    Cabin           object
    Embarked        object
    dtype: object




```python
df['Pclass'].dtype
```




    dtype('int64')




```python
df.loc[df['PassengerId']==51]
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
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>50</th>
      <td>51</td>
      <td>0</td>
      <td>3</td>
      <td>Panula, Master. Juha Niilo</td>
      <td>male</td>
      <td>7.0</td>
      <td>4</td>
      <td>1</td>
      <td>3101295</td>
      <td>39.6875</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.rename(columns={"PassengerId": "PassengerIndex"}, inplace=True)
```


```python
df
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
      <th>PassengerIndex</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>886</th>
      <td>887</td>
      <td>0</td>
      <td>2</td>
      <td>Montvila, Rev. Juozas</td>
      <td>male</td>
      <td>27.0</td>
      <td>0</td>
      <td>0</td>
      <td>211536</td>
      <td>13.0000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>887</th>
      <td>888</td>
      <td>1</td>
      <td>1</td>
      <td>Graham, Miss. Margaret Edith</td>
      <td>female</td>
      <td>19.0</td>
      <td>0</td>
      <td>0</td>
      <td>112053</td>
      <td>30.0000</td>
      <td>B42</td>
      <td>S</td>
    </tr>
    <tr>
      <th>888</th>
      <td>889</td>
      <td>0</td>
      <td>3</td>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
      <td>female</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>W./C. 6607</td>
      <td>23.4500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>889</th>
      <td>890</td>
      <td>1</td>
      <td>1</td>
      <td>Behr, Mr. Karl Howell</td>
      <td>male</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>111369</td>
      <td>30.0000</td>
      <td>C148</td>
      <td>C</td>
    </tr>
    <tr>
      <th>890</th>
      <td>891</td>
      <td>0</td>
      <td>3</td>
      <td>Dooley, Mr. Patrick</td>
      <td>male</td>
      <td>32.0</td>
      <td>0</td>
      <td>0</td>
      <td>370376</td>
      <td>7.7500</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 12 columns</p>
</div>




```python
df['Pclass'].unique()
```




    array([3, 1, 2], dtype=int64)




```python
df['Pclass'].unique().size
```




    3




```python
df.describe()
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
      <th>PassengerIndex</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>714.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>446.000000</td>
      <td>0.383838</td>
      <td>2.308642</td>
      <td>29.699118</td>
      <td>0.523008</td>
      <td>0.381594</td>
      <td>32.204208</td>
    </tr>
    <tr>
      <th>std</th>
      <td>257.353842</td>
      <td>0.486592</td>
      <td>0.836071</td>
      <td>14.526497</td>
      <td>1.102743</td>
      <td>0.806057</td>
      <td>49.693429</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.420000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>223.500000</td>
      <td>0.000000</td>
      <td>2.000000</td>
      <td>20.125000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>7.910400</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>446.000000</td>
      <td>0.000000</td>
      <td>3.000000</td>
      <td>28.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>14.454200</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>668.500000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>38.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>31.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>891.000000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>80.000000</td>
      <td>8.000000</td>
      <td>6.000000</td>
      <td>512.329200</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.shape
```




    (891, 12)




```python
df.describe().shape
```




    (8, 7)




```python
df.Fare.head()
```




    0     7.2500
    1    71.2833
    2     7.9250
    3    53.1000
    4     8.0500
    Name: Fare, dtype: float64




```python
df['Fare'].head()
```




    0     7.2500
    1    71.2833
    2     7.9250
    3    53.1000
    4     8.0500
    Name: Fare, dtype: float64




```python
df[['Fare','Age']].head()
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
      <th>Fare</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7.2500</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>71.2833</td>
      <td>38.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.9250</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>53.1000</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.0500</td>
      <td>35.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['Pclass'].unique() #[3, 1, 2]
df['Pclass'].unique().size
```




    3




```python
df['Embarked'].unique() #['S', 'C', 'Q', nan]
df['Embarked'].unique().size
```




    4




```python
df['Embarked'].describe()
```




    count     889
    unique      3
    top         S
    freq      644
    Name: Embarked, dtype: object




```python
df.loc[100]
df.loc[99:101]
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
      <th>PassengerIndex</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>99</th>
      <td>100</td>
      <td>0</td>
      <td>2</td>
      <td>Kantor, Mr. Sinai</td>
      <td>male</td>
      <td>34.0</td>
      <td>1</td>
      <td>0</td>
      <td>244367</td>
      <td>26.0000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>100</th>
      <td>101</td>
      <td>0</td>
      <td>3</td>
      <td>Petranec, Miss. Matilda</td>
      <td>female</td>
      <td>28.0</td>
      <td>0</td>
      <td>0</td>
      <td>349245</td>
      <td>7.8958</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>101</th>
      <td>102</td>
      <td>0</td>
      <td>3</td>
      <td>Petroff, Mr. Pastcho ("Pentcho")</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>349215</td>
      <td>7.8958</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[100]
```




    PassengerIndex                        101
    Survived                                0
    Pclass                                  3
    Name              Petranec, Miss. Matilda
    Sex                                female
    Age                                  28.0
    SibSp                                   0
    Parch                                   0
    Ticket                             349245
    Fare                               7.8958
    Cabin                                 NaN
    Embarked                                S
    Name: 100, dtype: object




```python
df.loc[100]
```




    PassengerIndex                        101
    Survived                                0
    Pclass                                  3
    Name              Petranec, Miss. Matilda
    Sex                                female
    Age                                  28.0
    SibSp                                   0
    Parch                                   0
    Ticket                             349245
    Fare                               7.8958
    Cabin                                 NaN
    Embarked                                S
    Name: 100, dtype: object




```python
df.set_index('PassengerIndex', inplace=True)
```


```python
df.loc[100] #user index
```




    Survived                    0
    Pclass                      2
    Name        Kantor, Mr. Sinai
    Sex                      male
    Age                      34.0
    SibSp                       1
    Parch                       0
    Ticket                 244367
    Fare                     26.0
    Cabin                     NaN
    Embarked                    S
    Name: 100, dtype: object




```python
df.iloc[100] #system index
```




    Survived                          0
    Pclass                            3
    Name        Petranec, Miss. Matilda
    Sex                          female
    Age                            28.0
    SibSp                             0
    Parch                             0
    Ticket                       349245
    Fare                         7.8958
    Cabin                           NaN
    Embarked                          S
    Name: 101, dtype: object




```python
df.loc[99:101]
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
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
    <tr>
      <th>PassengerIndex</th>
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
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>99</th>
      <td>1</td>
      <td>2</td>
      <td>Doling, Mrs. John T (Ada Julia Bone)</td>
      <td>female</td>
      <td>34.0</td>
      <td>0</td>
      <td>1</td>
      <td>231919</td>
      <td>23.0000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>100</th>
      <td>0</td>
      <td>2</td>
      <td>Kantor, Mr. Sinai</td>
      <td>male</td>
      <td>34.0</td>
      <td>1</td>
      <td>0</td>
      <td>244367</td>
      <td>26.0000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>101</th>
      <td>0</td>
      <td>3</td>
      <td>Petranec, Miss. Matilda</td>
      <td>female</td>
      <td>28.0</td>
      <td>0</td>
      <td>0</td>
      <td>349245</td>
      <td>7.8958</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.isnull().head()
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
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
    <tr>
      <th>PassengerIndex</th>
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
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>5</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.isnull().sum()
```




    Survived      0
    Pclass        0
    Name          0
    Sex           0
    Age         177
    SibSp         0
    Parch         0
    Ticket        0
    Fare          0
    Cabin       687
    Embarked      2
    dtype: int64




```python
df['newColumn'] = df['Survived'] + df['Pclass']
```


```python
df.shape
```




    (891, 12)




```python
df.head()
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
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>newColumn</th>
    </tr>
    <tr>
      <th>PassengerIndex</th>
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
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.reset_index(inplace=True)
```


```python
df.head()
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
      <th>PassengerIndex</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>newColumn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.drop(['newColumn'], axis = 1, inplace=True)
```


```python
df.head()
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
      <th>PassengerIndex</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
from jupyterthemes import get_themes
import jupyterthemes as jt
from jupyterthemes.stylefx import set_nb_theme
```


```python
set_nb_theme('monokai')
```




<style> div#notebook {
 font-family: sans-serif;
 font-size: 13pt;
 line-height: 170%;
 color: #f8f8f0;
 -webkit-font-smoothing: antialiased !important;
 padding-top: 25px !important;
}
body,
div.body {
 font-family: sans-serif;
 font-size: 13pt;
 color: #f8f8f0;
 background-color: #1e1e1e;
 background: #1e1e1e;
 -webkit-font-smoothing: antialiased !important;
}
body.notebook_app {
 padding: 0;
 background-color: #1e1e1e;
 background: #1e1e1e;
 padding-right: 0px !important;
 overflow-y: hidden;
}
a {
 font-family: sans-serif;
 color: #f8f8f0;
 -webkit-font-smoothing: antialiased !important;
}
a:hover,
a:focus {
 color: #f8f8f0;
 -webkit-font-smoothing: antialiased !important;
}
div#maintoolbar {
 position: absolute;
 width: 90%;
 margin-left: -10%;
 padding-right: 8%;
 float: left;
 background: transparent !important;
}
#maintoolbar {
 margin-bottom: -3px;
 margin-top: 0px;
 border: 0px;
 min-height: 27px;
 padding-top: 2px;
 padding-bottom: 0px;
}
#maintoolbar .container {
 width: 75%;
 margin-right: auto;
 margin-left: auto;
}
.list_header,
div#notebook_list_header.row.list_header {
 font-size: 14pt;
 color: #f8f8f0;
 background-color: transparent;
 height: 35px;
}
i.fa.fa-folder {
 display: inline-block;
 font: normal normal normal 14px "FontAwesome";
 font-family: "FontAwesome" !important;
 text-rendering: auto;
 -webkit-font-smoothing: antialiased;
 font-size: 18px;
 -moz-osx-font-smoothing: grayscale;
}
#running .panel-group .panel .panel-heading {
 font-size: 14pt;
 color: #f8f8f0;
 padding: 8px 8px;
 background: #2f2f2f;
 background-color: #2f2f2f;
}
#running .panel-group .panel .panel-heading a {
 font-size: 14pt;
 color: #f8f8f0;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
 font-size: 14pt;
 color: #f8f8f0;
}
#running .panel-group .panel .panel-body .list_container .list_item {
 background: #232323;
 background-color: #232323;
 padding: 2px;
 border-bottom: 2px solid rgba(93,92,82,.25);
}
#running .panel-group .panel .panel-body .list_container .list_item:hover {
 background: #232323;
 background-color: #232323;
}
#running .panel-group .panel .panel-body {
 padding: 2px;
}
button#refresh_running_list {
 border: none !important;
}
button#refresh_cluster_list {
 border: none !important;
}
div.running_list_info.toolbar_info {
 font-size: 15px;
 padding: 4px 0 4px 0;
 margin-top: 5px;
 margin-bottom: 8px;
 height: 24px;
 line-height: 24px;
 text-shadow: none;
}
.list_placeholder {
 font-weight: normal;
}
#tree-selector {
 padding: 0px;
 border-color: transparent;
}
#project_name > ul > li > a > i.fa.fa-home {
 color: #a6e22e;
 font-size: 17pt;
 display: inline-block;
 position: static;
 padding: 0px 0px;
 font-weight: normal;
 text-align: center;
 vertical-align: text-top;
}
.fa-folder:before {
 color: #ae81ff;
}
.fa-arrow-up:before {
 font-size: 14px;
}
.fa-arrow-down:before {
 font-size: 14px;
}
span#last-modified.btn.btn-xs.btn-default.sort-action:hover .fa,
span#sort-name.btn.btn-xs.btn-default.sort-action:hover .fa {
 color: #a6e22e;
}
.folder_icon:before {
 display: inline-block;
 font: normal normal normal 14px/1 FontAwesome;
 font-size: inherit;
 text-rendering: auto;
 -webkit-font-smoothing: antialiased;
 -moz-osx-font-smoothing: grayscale;
 content: "\f07b";
 color: #ae81ff;
}
.notebook_icon:before {
 display: inline-block;
 font: normal normal normal 14px/1 FontAwesome;
 font-size: inherit;
 text-rendering: auto;
 -webkit-font-smoothing: antialiased;
 -moz-osx-font-smoothing: grayscale;
 content: "\f02d";
 position: relative;
 color: #a6e22e !important;
 top: 0px;
}
.file_icon:before {
 display: inline-block;
 font: normal normal normal 14px/1 FontAwesome;
 font-size: inherit;
 text-rendering: auto;
 -webkit-font-smoothing: antialiased;
 -moz-osx-font-smoothing: grayscale;
 content: "\f15b";
 position: relative;
 top: 0px;
 color: #888888 !important;
}
#project_name a {
 display: inline-flex;
 padding-left: 7px;
 margin-left: -2px;
 text-align: -webkit-auto;
 vertical-align: baseline;
 font-size: 18px;
}
div#notebook_toolbar div.dynamic-instructions {
 font-family: sans-serif;
 font-size: 17px;
 color: #75715e;
}
span#login_widget > .button,
#logout {
 font-family: "Proxima Nova", sans-serif;
 color: #f8f8f0;
 background: transparent;
 background-color: transparent;
 border: 2px solid #2f2f2f;
 font-weight: normal;
 box-shadow: none;
 text-shadow: none;
 border-radius: 3px;
 margin-right: 10px;
 padding: 2px 7px;
}
span#login_widget > .button:hover,
#logout:hover {
 color: #a6e22e;
 background-color: transparent;
 background: transparent;
 border: 2px solid #a6e22e;
 background-image: none;
 box-shadow: none !important;
 border-radius: 3px;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus,
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
 color: #f8f8f2;
 background-color: #f8f8f0;
 background: #f8f8f0;
 border-color: #f8f8f0;
 background-image: none;
 box-shadow: none !important;
 border-radius: 2px;
}
body > #header #header-container {
 padding-bottom: 0px;
 padding-top: 4px;
 box-sizing: border-box;
 -moz-box-sizing: border-box;
 -webkit-box-sizing: border-box;
}
body > #header {
 background: #1e1e1e;
 background-color: #1e1e1e;
 position: relative;
 z-index: 100;
}
.list_container {
 font-size: 13pt;
 color: #f8f8f0;
 border: none;
 text-shadow: none !important;
}
.list_container > div {
 border-bottom: 1px solid rgba(93,92,82,.25);
 font-size: 13pt;
}
.list_header > div,
.list_item > div {
 padding-top: 6px;
 padding-bottom: 2px;
 padding-left: 0px;
}
.list_header > div .item_link,
.list_item > div .item_link {
 margin-left: -1px;
 vertical-align: middle;
 line-height: 22px;
 font-size: 13pt;
}
.item_icon {
 color: #ae81ff;
 font-size: 13pt;
 vertical-align: middle;
}
.list_item input:not([type="checkbox"]) {
 padding-right: 0px;
 height: 1.75em;
 width: 25%;
 margin: 0px 0 0;
 margin-top: 0px;
}
.list_header > div .item_link,
.list_item > div .item_link {
 margin-left: -1px;
 vertical-align: middle;
 line-height: 1.5em;
 font-size: 12pt;
 display: inline-table;
 position: static;
}
#button-select-all {
 height: 34px;
 min-width: 55px;
 z-index: 0;
 border: none !important;
 padding-top: 0px;
 padding-bottom: 0px;
 margin-bottom: 0px;
 margin-top: 0px;
 left: -3px;
 border-radius: 0px !important;
}
#button-select-all:focus,
#button-select-all:active:focus,
#button-select-all.active:focus,
#button-select-all.focus,
#button-select-all:active.focus,
#button-select-all.active.focus {
 background-color: #2f2f2f !important;
 background: #2f2f2f !important;
}
button#tree-selector-btn {
 height: 34px;
 font-size: 12.0pt;
 border: none;
 left: 0px;
 border-radius: 0px !important;
}
input#select-all.pull-left.tree-selector {
 margin-left: 7px;
 margin-right: 2px;
 margin-top: 2px;
 top: 4px;
}
input[type="radio"],
input[type="checkbox"] {
 margin-top: 1px;
 line-height: normal;
}
.delete-button {
 border: none !important;
}
i.fa.fa-trash {
 font-size: 13.5pt;
}
.list_container a {
 font-size: 16px;
 color: #f8f8f0;
 border: none;
 text-shadow: none !important;
 font-weight: normal;
 font-style: normal;
}
div.list_container a:hover {
 color: #f8f8f0;
}
.list_header > div input,
.list_item > div input {
 margin-right: 7px;
 margin-left: 12px;
 vertical-align: baseline;
 line-height: 22px;
 position: relative;
 top: -1px;
}
div.list_item:hover {
 background-color: rgba(93,92,82,.1);
}
.breadcrumb > li {
 font-size: 12.0pt;
 color: #f8f8f0;
 border: none;
 text-shadow: none !important;
}
.breadcrumb > li + li:before {
 content: "/\00a0";
 padding: 0px;
 color: #f8f8f0;
 font-size: 18px;
}
#project_name > .breadcrumb {
 padding: 0px;
 margin-bottom: 0px;
 background-color: transparent;
 font-weight: normal;
 margin-top: -2px;
}
ul#tabs a {
 font-family: sans-serif;
 font-size: 13.5pt;
 font-weight: normal;
 font-style: normal;
 text-shadow: none !important;
}
.nav-tabs {
 font-family: sans-serif;
 font-size: 13.5pt;
 font-weight: normal;
 font-style: normal;
 background-color: transparent;
 border-color: transparent;
 text-shadow: none !important;
 border: 2px solid transparent;
}
.nav-tabs > li > a:active,
.nav-tabs > li > a:focus,
.nav-tabs > li > a:hover,
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:focus,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
 color: #a6e22e;
 background-color: transparent;
 border-color: transparent;
 border-bottom: 2px solid transparent;
}
.nav > li.disabled > a,
.nav > li.disabled > a:hover {
 color: #75715e;
}
.nav-tabs > li > a:before {
 content: "";
 position: absolute;
 width: 100%;
 height: 2px;
 bottom: -2px;
 left: 0;
 background-color: #a6e22e;
 visibility: hidden;
 -webkit-transform: perspective(0)scaleX(0);
 transform: perspective(0)scaleX(0);
 -webkit-transition: ease 220ms;
 transition: ease 220ms;
 -webkit-font-smoothing: antialiased !important;
}
.nav-tabs > li > a:hover:before {
 visibility: visible;
 -webkit-transform: perspective(1)scaleX(1);
 transform: perspective(1)scaleX(1);
}
.nav-tabs > li.active > a:before {
 content: "";
 position: absolute;
 width: 100%;
 height: 2px;
 bottom: -2px;
 left: 0;
 background-color: #a6e22e;
 visibility: visible;
 -webkit-transform: perspective(1)scaleX(1);
 transform: perspective(1)scaleX(1);
 -webkit-font-smoothing: subpixel-antialiased !important;
}
div#notebook {
 font-family: sans-serif;
 font-size: 13pt;
 padding-top: 4px;
}
.notebook_app {
 background-color: #1e1e1e;
}
#notebook-container {
 padding: 13px 2px;
 background-color: #1e1e1e;
 min-height: 0px;
 box-shadow: none;
 width: 980px;
 margin-right: auto;
 margin-left: auto;
}
div#ipython-main-app.container {
 width: 980px;
 margin-right: auto;
 margin-left: auto;
 margin-right: auto;
 margin-left: auto;
}
.container {
 width: 980px;
 margin-right: auto;
 margin-left: auto;
}
div#menubar-container {
 width: 100%;
 width: 980px;
}
div#header-container {
 width: 980px;
}
.notebook_app #header,
.edit_app #header {
 box-shadow: none !important;
 background-color: #1e1e1e;
 border-bottom: 2px solid rgba(93,92,82,.25);
}
#header,
.edit_app #header {
 font-family: sans-serif;
 font-size: 13pt;
 box-shadow: none;
 background-color: #1e1e1e;
}
#header .header-bar,
.edit_app #header .header-bar {
 background: #1e1e1e;
 background-color: #1e1e1e;
}
body > #header .header-bar {
 width: 100%;
 background: #1e1e1e;
}
span.checkpoint_status,
span.autosave_status {
 font-size: small;
 display: none;
}
#menubar,
div#menubar {
 background-color: #1e1e1e;
 padding-top: 0px !important;
}
#menubar .navbar,
.navbar-default {
 background-color: #1e1e1e;
 margin-bottom: 0px;
 margin-top: 0px;
}
.navbar {
 border: none;
}
div.navbar-text,
.navbar-text,
.navbar-text.indicator_area,
p.navbar-text.indicator_area {
 margin-top: 8px !important;
 margin-bottom: 0px;
 color: #a6e22e;
}
.navbar-default {
 font-family: sans-serif;
 font-size: 13pt;
 background-color: #1e1e1e;
 border-color: rgba(93,92,82,.25);
 line-height: 1.5em;
 padding-bottom: 0px;
}
.navbar-default .navbar-nav > li > a {
 font-family: sans-serif;
 font-size: 13pt;
 color: #f8f8f0;
 display: block;
 line-height: 1.5em;
 padding-top: 14px;
 padding-bottom: 11px;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
 color: #f8f8f0 !important;
 background-color: rgba(93,92,82,.25) !important;
 border-color: rgba(93,92,82,.25) !important;
 line-height: 1.5em;
 transition: 80ms ease;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
 color: #f8f8f2;
 background-color: #383838;
 border-color: #383838;
 line-height: 1.5em;
}
.navbar-nav > li > .dropdown-menu {
 margin-top: 0px;
}
.navbar-nav {
 margin: 0;
}
div.notification_widget.info,
.notification_widget.info,
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus,
div#notification_notebook.notification_widget.btn.btn-xs.navbar-btn,
div#notification_notebook.notification_widget.btn.btn-xs.navbar-btn:hover,
div#notification_notebook.notification_widget.btn.btn-xs.navbar-btn:focus {
 color: #f8f8f0 !important;
 background-color: transparent !important;
 border-color: transparent !important;
 padding-bottom: 0px !important;
 margin-bottom: 0px !important;
 font-size: 9pt !important;
 z-index: 0;
}
div#notification_notebook.notification_widget.btn.btn-xs.navbar-btn {
 font-size: 9pt !important;
 z-index: 0;
}
.notification_widget {
 color: #ae81ff;
 z-index: -500;
 font-size: 9pt;
 background: transparent;
 background-color: transparent;
 margin-right: 3px;
 border: none;
}
.notification_widget,
div.notification_widget {
 margin-right: 0px;
 margin-left: 0px;
 padding-right: 0px;
 vertical-align: text-top !important;
 margin-top: 6px !important;
 background: transparent !important;
 background-color: transparent !important;
 font-size: 9pt !important;
 border: none;
}
.navbar-btn.btn-xs:hover {
 border: none !important;
 background: transparent !important;
 background-color: transparent !important;
 color: #f8f8f0 !important;
}
div.notification_widget.info,
.notification_widget.info {
 display: none !important;
}
.edit_mode .modal_indicator:before {
 display: none;
}
.command_mode .modal_indicator:before {
 display: none;
}
.item_icon {
 color: #ae81ff;
}
.item_buttons .kernel-name {
 font-size: 13pt;
 color: #ae81ff;
}
.running_notebook_icon:before {
 color: #a6e22e !important;
 font: normal normal normal 15px/1 FontAwesome;
 font-size: 15px;
 text-rendering: auto;
 -webkit-font-smoothing: antialiased;
 -moz-osx-font-smoothing: grayscale;
 content: "\f10c";
 vertical-align: middle;
 position: static;
 display: inherit;
}
.item_buttons .running-indicator {
 padding-top: 4px;
 color: #a6e22e;
 font-family: sans-serif;
 text-rendering: auto;
 -webkit-font-smoothing: antialiased;
}
#notification_trusted {
 font-family: sans-serif;
 border: none;
 background: transparent;
 background-color: transparent;
 margin-bottom: 0px !important;
 vertical-align: bottom !important;
 color: #75715e !important;
 cursor: default !important;
}
#notification_area,
div.notification_area {
 float: right !important;
 position: static;
 cursor: pointer;
 padding-top: 6px;
 padding-right: 4px;
}
div#notification_notebook.notification_widget.btn.btn-xs.navbar-btn {
 font-size: 9pt !important;
 z-index: 0;
 margin-top: -5px !important;
}
#modal_indicator {
 float: right !important;
 color: #4c8be2;
 background: #1e1e1e;
 background-color: #1e1e1e;
 margin-top: 8px !important;
 margin-left: 0px;
}
#kernel_indicator {
 float: right !important;
 color: #a6e22e;
 background: #1e1e1e;
 background-color: #1e1e1e;
 border-left: 2px solid #a6e22e;
 padding-top: 0px;
 padding-bottom: 4px;
 margin-top: 10px !important;
 margin-left: -2px;
 padding-left: 5px !important;
}
#kernel_indicator .kernel_indicator_name {
 font-size: 17px;
 color: #a6e22e;
 background: #1e1e1e;
 background-color: #1e1e1e;
 padding-left: 5px;
 padding-right: 5px;
 margin-top: 4px;
 vertical-align: text-top;
 padding-bottom: 0px;
}
.kernel_idle_icon:before {
 display: inline-block;
 font: normal normal normal 22px/1 FontAwesome;
 font-size: 22px;
 text-rendering: auto;
 -webkit-font-smoothing: antialiased;
 cursor: pointer;
 margin-left: 0px !important;
 opacity: 0.7;
 vertical-align: bottom;
 margin-top: 1px;
 content: "\f1db";
}
.kernel_busy_icon:before {
 display: inline-block;
 font: normal normal normal 22px/1 FontAwesome;
 font-size: 22px;
 -webkit-animation: pulsate 2s infinite ease-out;
 animation: pulsate 2s infinite ease-out;
 text-rendering: auto;
 -webkit-font-smoothing: antialiased;
 cursor: pointer;
 margin-left: 0px !important;
 vertical-align: bottom;
 margin-top: 1px;
 content: "\f111";
}
@-webkit-keyframes pulsate {
 0% {
  -webkit-transform: scale(1.0,1.0);
  opacity: 0.8;
 }
 8% {
  -webkit-transform: scale(1.0,1.0);
  opacity: 0.8;
 }
 50% {
  -webkit-transform: scale(0.75,0.75);
  opacity: 0.3;
 }
 92% {
  -webkit-transform: scale(1.0,1.0);
  opacity: 0.8;
 }
 100% {
  -webkit-transform: scale(1.0,1.0);
  opacity: 0.8;
 }
}
div.notification_widget.info,
.notification_widget.info,
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus,
div#notification_notebook.notification_widget.btn.btn-xs.navbar-btn,
div#notification_notebook.notification_widget.btn.btn-xs.navbar-btn:hover,
div#notification_notebook.notification_widget.btn.btn-xs.navbar-btn:focus {
 color: #f8f8f0;
 background-color: #1e1e1e;
 border-color: #1e1e1e;
}
#notification_area,
div.notification_area {
 float: right !important;
 position: static;
}
.notification_widget,
div.notification_widget {
 margin-right: 0px;
 margin-left: 0px;
 padding-right: 0px;
 vertical-align: text-top !important;
 margin-top: 6px !important;
 z-index: 1000;
}
#kernel_logo_widget,
#kernel_logo_widget .current_kernel_logo {
 display: none;
}
div#ipython_notebook {
 display: none;
}
i.fa.fa-icon {
 -webkit-font-smoothing: antialiased;
 -moz-osx-font-smoothing: grayscale;
 text-rendering: auto;
}
.fa {
 display: inline-block;
 font: normal normal normal 10pt/1 "FontAwesome", sans-serif;
 text-rendering: auto;
 -webkit-font-smoothing: antialiased;
 -moz-osx-font-smoothing: grayscale;
}
.dropdown-menu {
 font-family: sans-serif;
 font-size: 13pt;
 box-shadow: none;
 padding: 0px;
 text-align: left;
 border: none;
 background-color: #383838;
 background: #383838;
 line-height: 1;
}
.dropdown-menu:hover {
 font-family: sans-serif;
 font-size: 13pt;
 box-shadow: none;
 padding: 0px;
 text-align: left;
 border: none;
 background-color: #383838;
 box-shadow: none;
 line-height: 1;
}
.dropdown-menu > li > a {
 font-family: sans-serif;
 font-size: 12.0pt;
 display: block;
 padding: 10px 20px 9px 10px;
 color: #f8f8f0;
 background-color: #383838;
 background: #383838;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
 color: #f8f8f0;
 background-color: rgba(93,92,82,.25);
 background: rgba(93,92,82,.25);
 border-color: rgba(93,92,82,.25);
 transition: 200ms ease;
}
.dropdown-menu .divider {
 height: 1px;
 margin: 0px 0px;
 overflow: hidden;
 background-color: rgba(93,92,82,.5);
}
.dropdown-submenu > .dropdown-menu {
 display: none;
 top: 2px !important;
 left: 100%;
 margin-top: -2px;
 margin-left: 0px;
 padding-top: 0px;
 transition: 200ms ease;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
 font-family: sans-serif;
 font-size: 12.0pt;
 font-weight: normal;
 color: #75715e;
 padding: none;
 display: block;
 clear: both;
 white-space: nowrap;
}
.dropdown-submenu > a:after {
 color: #f8f8f0;
 margin-right: -16px;
 margin-top: 0px;
 display: inline-block;
}
.dropdown-submenu:hover > a:after,
.dropdown-submenu:active > a:after,
.dropdown-submenu:focus > a:after,
.dropdown-submenu:visited > a:after {
 color: #a6e22e;
 margin-right: -16px;
 display: inline-block !important;
}
div.kse-dropdown > .dropdown-menu,
.kse-dropdown > .dropdown-menu {
 min-width: 0;
 top: 94%;
}
.btn,
.btn-default {
 font-family: sans-serif;
 color: #f8f8f0;
 background: #2f2f2f;
 background-color: #2f2f2f;
 border: 2px solid #2f2f2f;
 font-weight: normal;
 box-shadow: none;
 text-shadow: none;
 border-radius: 3px;
 font-size: initial;
}
.btn:hover,
.btn:active:hover,
.btn.active:hover,
.btn-default:hover,
.open > .dropdown-toggle.btn-default:hover,
.open > .dropdown-toggle.btn:hover {
 color: #a6e22e;
 border: 2px solid #2a2a2a;
 background-color: #2a2a2a;
 background: #2a2a2a;
 background-image: none;
 box-shadow: none !important;
 border-radius: 3px;
}
.btn:active,
.btn.active,
.btn:active:focus,
.btn.active:focus,
.btn:active.focus,
.btn.active.focus,
.btn-default:focus,
.btn-default.focus,
.btn-default:active,
.btn-default.active,
.btn-default:active:hover,
.btn-default.active:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn:focus,
.open > .dropdown-toggle.btn.focus,
.open > .dropdown-toggle.btn-default:hover,
.open > .dropdown-toggle.btn-default:focus,
.open > .dropdown-toggle.btn-default.hover,
.open > .dropdown-toggle.btn-default.focus {
 color: #a6e22e;
 border: 2px solid #2a2a2a;
 background-color: #2a2a2a !important;
 background: #2a2a2a !important;
 background-image: none;
 box-shadow: none !important;
 border-radius: 3px;
}
.btn-default:active:hover,
.btn-default.active:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.btn-default:active.focus,
.btn-default.active.focus {
 color: #a6e22e !important;
 background-color: #2f2f2f;
 border-color: #546745 !important;
 transition: 2000ms ease;
}
.btn:focus,
.btn.focus,
.btn:active:focus,
.btn.active:focus,
.btn:active,
.btn.active,
.btn:active.focus,
.btn.active.focus {
 color: #a6e22e !important;
 outline: none !important;
 outline-width: 0px !important;
 background: #546745 !important;
 background-color: #546745 !important;
 border-color: #546745 !important;
 transition: 200ms ease !important;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
 font-size: 13pt;
 background: transparent;
 background-color: transparent;
 border: 0px solid #2f2f2f;
 border-bottom: 2px solid transparent;
 margin-left: 5px;
 padding-top: 4px !important;
}
.item_buttons > .btn:hover,
.item_buttons > .btn-group:hover,
.item_buttons > .input-group:hover,
.item_buttons > .btn.active,
.item_buttons > .btn-group.active,
.item_buttons > .input-group.active,
.item_buttons > .btn.focus {
 margin-left: 5px;
 background: #2a2a2a;
 padding-top: 4px !important;
 background-color: transparent;
 border: 0px solid transparent;
 border-bottom: 2px solid #a6e22e;
 border-radius: 0px;
 transition: none;
}
.item_buttons {
 line-height: 1.5em !important;
}
.item_buttons .btn {
 min-width: 11ex;
}
.btn-group > .btn:first-child {
 margin-left: 3px;
}
.btn-group > .btn-mini,
.btn-sm,
.btn-group-sm > .btn,
.btn-xs,
.btn-group-xs > .btn,
.alternate_upload .btn-upload,
.btn-group,
.btn-group-vertical {
 font-size: inherit;
 font-weight: normal;
 height: inherit;
 line-height: inherit;
}
.btn-xs,
.btn-group-xs > .btn {
 font-size: initial !important;
 background-image: none;
 font-weight: normal;
 text-shadow: none;
 display: inline-table;
 padding: 2px 5px;
 line-height: 1.45;
}
.btn-group > .btn:first-child {
 margin-left: 3px;
}
div#new-buttons > button,
#new-buttons > button,
div#refresh_notebook_list,
#refresh_notebook_list {
 background: transparent;
 background-color: transparent;
 border: none;
}
div#new-buttons > button:hover,
#new-buttons > button:hover,
div#refresh_notebook_list,
#refresh_notebook_list,
div.alternate_upload .btn-upload,
.alternate_upload .btn-upload,
div.dynamic-buttons > button,
.dynamic-buttons > button,
.dynamic-buttons > button:focus,
.dynamic-buttons > button:active:focus,
.dynamic-buttons > button.active:focus,
.dynamic-buttons > button.focus,
.dynamic-buttons > button:active.focus,
.dynamic-buttons > button.active.focus,
#new-buttons > button:focus,
#new-buttons > button:active:focus,
#new-buttons > button.active:focus,
#new-buttons > button.focus,
#new-buttons > button:active.focus,
#new-buttons > button.active.focus,
.alternate_upload .btn-upload:focus,
.alternate_upload .btn-upload:active:focus,
.alternate_upload .btn-upload.active:focus,
.alternate_upload .btn-upload.focus,
.alternate_upload .btn-upload:active.focus,
.alternate_upload .btn-upload.active.focus {
 background: transparent !important;
 background-color: transparent !important;
 border: none !important;
}
.alternate_upload input.fileinput {
 text-align: center;
 vertical-align: bottom;
 margin-left: -.5ex;
 display: inline-table;
 border: solid 0px #2f2f2f;
 margin-bottom: -1ex;
}
.alternate_upload .btn-upload {
 display: inline-table;
 background: transparent;
 border: none;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
 margin-left: -2px;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
 border-bottom-right-radius: 0;
 border-top-right-radius: 0;
 z-index: 2;
}
.dropdown-header {
 font-family: sans-serif !important;
 font-size: 13pt !important;
 color: #a6e22e !important;
 border-bottom: none !important;
 padding: 0px !important;
 margin: 6px 6px 0px !important;
}
span#last-modified.btn.btn-xs.btn-default.sort-action,
span#sort-name.btn.btn-xs.btn-default.sort-action,
span#file-size.btn.btn-xs.btn-default.sort-action {
 font-family: sans-serif;
 font-size: 16px;
 background-color: transparent;
 background: transparent;
 border: none;
 color: #f8f8f0;
 padding-bottom: 0px;
 margin-bottom: 0px;
 vertical-align: sub;
}
span#last-modified.btn.btn-xs.btn-default.sort-action {
 margin-left: 19px;
}
button.close {
 border: 0px none;
 font-family: sans-serif;
 font-size: 20pt;
 font-weight: normal;
}
.dynamic-buttons {
 padding-top: 0px;
 display: inline-block;
}
.close {
 color: #f92672;
 opacity: .5;
 text-shadow: none;
 font-weight: normal;
}
.close:hover {
 color: #f92672;
 opacity: 1;
 font-weight: normal;
}
div.nbext-enable-btns .btn[disabled],
div.nbext-enable-btns .btn[disabled]:hover,
.btn-default.disabled,
.btn-default[disabled],
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
 color: #888888;
 background: #2c2c2c;
 background-color: #2c2c2c;
 border-color: #2c2c2c;
 transition: 200ms ease;
}
.input-group-addon {
 padding: 2px 5px;
 font-size: 13pt;
 font-weight: normal;
 height: auto;
 color: #f8f8f0;
 text-align: center;
 background-color: transparent;
 border: 2px solid transparent !important;
 text-transform: capitalize;
}
a.btn.btn-default.input-group-addon:hover {
 background: transparent !important;
 background-color: transparent !important;
}
.btn-group > .btn + .dropdown-toggle {
 padding-left: 8px;
 padding-right: 8px;
 height: 100%;
}
.btn-group > .btn + .dropdown-toggle:hover {
 background: #2a2a2a !important;
}
.input-group-btn {
 position: relative;
 font-size: inherit;
 white-space: nowrap;
 background: #2f2f2f;
 background-color: #2f2f2f;
 border: none;
}
.input-group-btn:hover {
 background: #2a2a2a;
 background-color: #2a2a2a;
 border: none;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
 background: #2f2f2f;
 background-color: #2f2f2f;
 border: none;
 margin-left: 2px;
 margin-right: -1px;
 font-size: inherit;
}
.input-group-btn:first-child > .btn:hover,
.input-group-btn:first-child > .btn-group:hover {
 background: #2a2a2a;
 background-color: #2a2a2a;
 border: none;
 font-size: inherit;
 transition: 200ms ease;
}
div.modal .btn-group > .btn:first-child {
 background: #2f2f2f;
 background-color: #2f2f2f;
 border: 1px solid #2c2c2c;
 margin-top: 0px !important;
 margin-left: 0px;
 margin-bottom: 2px;
}
div.modal .btn-group > .btn:first-child:hover {
 background: #2a2a2a;
 background-color: #2a2a2a;
 border: 1px solid #2a2a2a;
 transition: 200ms ease;
}
div.modal > button,
div.modal-footer > button {
 background: #2f2f2f;
 background-color: #2f2f2f;
 border-color: #2f2f2f;
}
div.modal > button:hover,
div.modal-footer > button:hover {
 background: #2a2a2a;
 background-color: #2a2a2a;
 border-color: #2a2a2a;
 transition: 200ms ease;
}
.modal-content {
 font-family: sans-serif;
 font-size: 12.0pt;
 position: relative;
 background: #2f2f2f;
 background-color: #2f2f2f;
 border: none;
 border-radius: 1px;
 background-clip: padding-box;
 outline: none;
}
.modal-header {
 font-family: sans-serif;
 font-size: 13pt;
 color: #f8f8f0;
 background: #2f2f2f;
 background-color: #2f2f2f;
 border-color: rgba(93,92,82,.25);
 padding: 12px;
 min-height: 16.4286px;
}
.modal-content h4 {
 font-family: sans-serif;
 font-size: 16pt;
 color: #f8f8f0;
 padding: 5px;
}
.modal-body {
 background-color: #232323;
 position: relative;
 padding: 15px;
}
.modal-footer {
 padding: 8px;
 text-align: right;
 background-color: #232323;
 border-top: none;
}
.alert-info {
 background-color: #2f2f2f;
 border-color: rgba(93,92,82,.25);
 color: #f8f8f0;
}
.modal-header .close {
 margin-top: -5px;
 font-size: 25pt;
}
.modal-backdrop,
.modal-backdrop.in {
 opacity: 0.85;
 background-color: notebook-bg;
}
div.panel,
div.panel-default,
.panel,
.panel-default {
 font-family: sans-serif;
 font-size: 13pt;
 background-color: #232323;
 color: #f8f8f0;
 margin-bottom: 14px;
 border: 0;
 box-shadow: none;
}
div.panel > .panel-heading,
div.panel-default > .panel-heading {
 font-size: 14pt;
 color: #f8f8f0;
 background: #2f2f2f;
 background-color: #2f2f2f;
 border: 0;
}
.modal .modal-dialog {
 min-width: 950px;
 margin: 50px auto;
}
div.container-fluid {
 margin-right: auto;
 margin-left: auto;
 padding-left: 0px;
 padding-right: 5px;
}
div.form-control,
.form-control {
 font-family: sans-serif;
 font-size: initial;
 color: #f8f8f0;
 background-color: #282828;
 border: 1px solid #282828 !important;
 margin-left: 2px;
 box-shadow: none;
 transition: border-color 0.15s ease-in-out 0s, box-shadow 0.15s ease-in-out 0s;
}
.form-control-static {
 min-height: inherit;
 height: inherit;
}
.form-group.list-group-item {
 color: #f8f8f0;
 background-color: #232323;
 border-color: rgba(93,92,82,.25);
 margin-bottom: 0px;
}
.form-group .input-group {
 float: left;
}
input,
button,
select,
textarea {
 background-color: #282828;
 font-weight: normal;
 border: 1px solid rgba(93,92,82,.25);
}
select.form-control.select-xs {
 height: 33px;
 font-size: 13pt;
}
.toolbar select,
.toolbar label {
 width: auto;
 vertical-align: middle;
 margin-right: 0px;
 margin-bottom: 0px;
 display: inline;
 font-size: 92%;
 margin-left: 10px;
 padding: 0px;
 background: #2f2f2f !important;
 background-color: #2f2f2f !important;
 border: 2px solid #2f2f2f !important;
}
.form-control:focus {
 border-color: #a6e22e;
 outline: 2px solid #49483e;
 -webkit-box-shadow: none;
}
::-webkit-input-placeholder {
 color: #75715e;
}
::-moz-placeholder {
 color: #75715e;
}
:-ms-input-placeholder {
 color: #75715e;
}
:-moz-placeholder {
 color: #75715e;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
 border: 2px solid rgba(93,92,82,.25) !important;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control:focus {
 border-color: #a6e22e;
 outline: 2px solid #49483e;
 -webkit-box-shadow: none;
 box-shadow: none;
}
div.output.output_scroll {
 box-shadow: none;
}
::-webkit-scrollbar {
 width: 11px;
 max-height: 9px;
 background-color: #2d2d2d;
 border-radius: 3px;
 border: none;
}
::-webkit-scrollbar-track {
 background: #2d2d2d;
 border: none;
 width: 11px;
 max-height: 9px;
}
::-webkit-scrollbar-thumb {
 border-radius: 2px;
 border: none;
 background: #49483e;
 background-clip: content-box;
 width: 11px;
}
HTML,
body,
div,
dl,
dt,
dd,
ul,
ol,
li,
h1,
h2,
h3,
h4,
h5,
h6,
pre,
code,
form,
fieldset,
legend,
input,
button,
textarea,
p,
blockquote,
th,
td,
span,
a {
 text-rendering: geometricPrecision;
 -webkit-font-smoothing: subpixel-antialiased;
 font-weight: 400;
}
div.input_area {
 background-color: #282828;
 background: #282828;
 padding-right: 1.2em;
 border: 0px;
 border-radius: 0px;
 border-top-right-radius: 4px;
 border-bottom-right-radius: 4px;
}
div.cell {
 padding: 0px;
 background: #282828;
 background-color: #282828;
 border: medium solid #1e1e1e;
 border-radius: 4px;
 top: 0;
}
div.cell.selected {
 background: #282828;
 background-color: #282828;
 border: medium solid #1e1e1e;
 padding: 0px;
 border-radius: 5px;
}
.edit_mode div.cell.selected {
 padding: 0px;
 background: #282828;
 background-color: #282828;
 border: medium solid #1e1e1e;
 border-radius: 5px;
}
div.cell.edit_mode {
 padding: 0px;
 background: #282828;
 background-color: #282828;
}
div.CodeMirror-sizer {
 margin-left: 0px;
 margin-bottom: -21px;
 border-right-width: 16px;
 min-height: 37px;
 padding-right: 0px;
 padding-bottom: 0px;
 margin-top: 0px;
}
div.cell.selected:before,
.edit_mode div.cell.selected:before,
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
 background: #282828 !important;
 border: none;
 border-radius: 3px;
 position: absolute;
 display: block;
 top: 0px;
 left: 0px;
 width: 0px;
 height: 100%;
}
div.cell.text_cell.selected::before,
.edit_mode div.cell.text_cell.selected:before,
div.cell.text_cell.selected:before,
div.cell.text_cell.selected.jupyter-soft-selected:before {
 background: #282828 !important;
 background-color: #282828 !important;
 border-color: #57564b !important;
}
div.cell.code_cell .input {
 border-left: 5px solid #282828 !important;
 border-radius: 3px;
 border-bottom-left-radius: 3px;
 border-top-left-radius: 3px;
}
div.cell.code_cell.selected .input {
 border-left: 5px solid #57564b !important;
 border-radius: 3px;
}
.edit_mode div.cell.code_cell.selected .input {
 border-left: 5px solid #33322b !important;
 border-radius: 3px;
}
.edit_mode div.cell.selected:before {
 height: 100%;
 border-left: 5px solid #33322b !important;
 border-radius: 3px;
}
div.cell.jupyter-soft-selected,
div.cell.selected.jupyter-soft-selected {
 border-left-color: #33322b !important;
 border-left-width: 0px !important;
 padding-left: 7px !important;
 border-right-color: #33322b !important;
 border-right-width: 0px !important;
 background: #33322b !important;
 border-radius: 6px !important;
}
div.cell.selected.jupyter-soft-selected .input {
 border-left: 5px solid #282828 !important;
}
div.cell.selected.jupyter-soft-selected {
 border-left-color: #57564b;
 border-color: #1e1e1e;
 padding-left: 7px;
 border-radius: 6px;
}
div.cell.code_cell.selected .input {
 border-left: none;
 border-radius: 3px;
}
div.cell.selected.jupyter-soft-selected .prompt,
div.cell.text_cell.selected.jupyter-soft-selected .prompt {
 top: 0;
 border-left: #282828 !important;
 border-radius: 2px;
}
div.cell.text_cell.selected.jupyter-soft-selected .input_prompt {
 border-left: none !important;
}
div.cell.text_cell.jupyter-soft-selected,
div.cell.text_cell.selected.jupyter-soft-selected {
 border-left-color: #33322b !important;
 border-left-width: 0px !important;
 padding-left: 26px !important;
 border-right-color: #33322b !important;
 border-right-width: 0px !important;
 background: #33322b !important;
 border-radius: 5px !important;
}
div.cell.jupyter-soft-selected .input,
div.cell.selected.jupyter-soft-selected .input {
 border-left-color: #33322b !important;
}
div.prompt,
.prompt {
 font-family: monospace, monospace;
 font-size: 9pt !important;
 font-weight: normal;
 color: #75715e;
 line-height: 170%;
 padding: 0px;
 padding-top: 4px;
 padding-left: 0px;
 padding-right: 1px;
 text-align: right !important;
 min-width: 11.5ex !important;
 width: 11.5ex !important;
}
div.prompt.input_prompt {
 font-size: 9pt !important;
 background-color: #282828;
 border-top: 0px;
 border-top-right-radius: 0px;
 border-bottom-left-radius: 0px;
 border-bottom-right-radius: 0px;
 padding-right: 3px;
 min-width: 11.5ex;
 width: 11.5ex !important;
}
div.cell.code_cell .input_prompt {
 border-right: 2px solid #49483e;
}
div.cell.selected .prompt {
 top: 0;
}
.edit_mode div.cell.selected .prompt {
 top: 0;
}
.edit_mode div.cell.selected .prompt {
 top: 0;
}
.run_this_cell {
 visibility: hidden;
 color: transparent;
 padding-top: 0px;
 padding-bottom: 0px;
 padding-left: 3px;
 padding-right: 12px;
 width: 1.5ex;
 width: 0ex;
 background: transparent;
 background-color: transparent;
}
div.code_cell:hover div.input .run_this_cell {
 visibility: visible;
}
div.cell.code_cell.rendered.selected .run_this_cell:hover {
 background-color: #1e1e1e;
 background: #1e1e1e;
 color: #57564b !important;
}
div.cell.code_cell.rendered.unselected .run_this_cell:hover {
 background-color: #1e1e1e;
 background: #1e1e1e;
 color: #57564b !important;
}
i.fa-step-forward.fa {
 display: inline-block;
 font: normal normal normal 9px "FontAwesome";
}
.fa-step-forward:before {
 content: "\f04b";
}
div.cell.selected.jupyter-soft-selected .run_this_cell,
div.cell.selected.jupyter-soft-selected .run_this_cell:hover,
div.cell.unselected.jupyter-soft-selected .run_this_cell:hover,
div.cell.code_cell.rendered.selected.jupyter-soft-selected .run_this_cell:hover,
div.cell.code_cell.rendered.unselected.jupyter-soft-selected .run_this_cell:hover {
 background-color: #33322b !important;
 background: #33322b !important;
 color: #33322b !important;
}
div.output_wrapper {
 background-color: #232323;
 border: 0px;
 left: 0px;
 margin-bottom: 0em;
 margin-top: 0em;
 border-top-right-radius: 0px;
 border-top-left-radius: 0px;
}
div.output_subarea.output_text.output_stream.output_stdout,
div.output_subarea.output_text {
 font-family: monospace, monospace;
 font-size: 8.5pt !important;
 line-height: 150% !important;
 background-color: #232323;
 color: #cccccc;
 border-top-right-radius: 0px;
 border-top-left-radius: 0px;
 margin-left: 11.5px;
}
div.output_area pre {
 font-family: monospace, monospace;
 font-size: 8.5pt !important;
 line-height: 151% !important;
 color: #cccccc;
 border-top-right-radius: 0px;
 border-top-left-radius: 0px;
}
div.output_area {
 display: -webkit-box;
}
div.output_html {
 font-family: monospace, monospace;
 font-size: 8.5pt;
 color: #cccccc;
 background-color: #232323;
 background: #232323;
}
div.output_subarea {
 overflow-x: auto;
 padding: 1.2em !important;
 -webkit-box-flex: 1;
 -moz-box-flex: 1;
 box-flex: 1;
 flex: 1;
}
div.btn.btn-default.output_collapsed {
 background: #222222;
 background-color: #222222;
 border-color: #222222;
}
div.btn.btn-default.output_collapsed:hover {
 background: #1d1d1d;
 background-color: #1d1d1d;
 border-color: #1d1d1d;
}
div.prompt.output_prompt {
 font-family: monospace, monospace;
 font-weight: bold !important;
 background-color: #232323;
 color: transparent;
 border-bottom-left-radius: 4px;
 border-top-right-radius: 0px;
 border-top-left-radius: 0px;
 border-bottom-right-radius: 0px;
 min-width: 11.5ex !important;
 width: 11.5ex !important;
 border-right: 2px solid transparent;
}
div.out_prompt_overlay.prompt {
 font-family: monospace, monospace;
 font-weight: bold !important;
 background-color: #232323;
 border-bottom-left-radius: 2px;
 border-top-right-radius: 0px;
 border-top-left-radius: 0px;
 border-bottom-right-radius: 0px;
 min-width: 11.5ex !important;
 width: 11.5ex !important;
 border-right: 2px solid transparent;
 color: transparent;
}
div.out_prompt_overlay.prompt:hover {
 background-color: #49483e;
 box-shadow: none !important;
 border: none;
 border-bottom-left-radius: 2px;
 -webkit-border-: 2px;
 -moz-border-radius: 2px;
 border-top-right-radius: 0px;
 border-top-left-radius: 0px;
 min-width: 11.5ex !important;
 width: 11.5ex !important;
 border-right: 2px solid #49483e !important;
}
div.cell.code_cell .output_prompt {
 border-right: 2px solid transparent;
 color: transparent;
}
div.cell.selected .output_prompt,
div.cell.selected .out_prompt_overlay.prompt {
 border-left: 5px solid #33322b;
 border-right: 2px solid #232323;
 border-radius: 0px !important;
}
.edit_mode div.cell.selected .output_prompt,
.edit_mode div.cell.selected .out_prompt_overlay.prompt {
 border-left: 5px solid #33322b;
 border-right: 2px solid #232323;
 border-radius: 0px !important;
}
div.text_cell,
div.text_cell_render pre,
div.text_cell_render {
 font-family: sans-serif;
 font-size: 13pt;
 line-height: 130% !important;
 color: #f8f8f0;
 background: #282828;
 background-color: #282828;
 border-radius: 0px;
}
div .text_cell_render {
 padding: 0.4em 0.4em 0.4em 0.4em;
}
div.cell.text_cell .CodeMirror-lines {
 padding-top: .7em !important;
 padding-bottom: .4em !important;
 padding-left: .5em !important;
 padding-right: .5em !important;
 margin-top: .4em;
 margin-bottom: .3em;
}
div.cell.text_cell.unrendered div.input_area,
div.cell.text_cell.rendered div.input_area {
 background-color: #282828;
 background: #282828;
 border: 0px;
 border-radius: 2px;
}
div.cell.text_cell .CodeMirror,
div.cell.text_cell .CodeMirror pre {
 line-height: 170% !important;
}
div.cell.text_cell.rendered.selected {
 font-family: sans-serif;
 line-height: 170% !important;
 background: #282828;
 background-color: #282828;
 border-radius: 0px;
}
div.cell.text_cell.unrendered.selected {
 font-family: sans-serif;
 line-height: 170% !important;
 background: #282828;
 background-color: #282828;
 border-radius: 0px;
}
div.cell.text_cell.selected {
 font-family: sans-serif;
 line-height: 170% !important;
 background: #282828;
 background-color: #282828;
 border-radius: 0px;
}
.edit_mode div.cell.text_cell.selected {
 font-family: sans-serif;
 line-height: 170% !important;
 background: #282828;
 background-color: #282828;
 border-radius: 0px;
}
div.text_cell.unrendered,
div.text_cell.unrendered.selected,
div.edit_mode div.text_cell.unrendered {
 font-family: sans-serif;
 line-height: 170% !important;
 background: #282828;
 background-color: #282828;
 border-radius: 0px;
}
div.cell.text_cell .prompt {
 border-right: 0;
 min-width: 11.5ex !important;
 width: 11.5ex !important;
}
div.cell.text_cell.rendered .prompt {
 font-family: monospace, monospace;
 font-size: 9.5pt !important;
 font-weight: normal;
 color: #75715e !important;
 text-align: right !important;
 min-width: 14.5ex !important;
 width: 14.5ex !important;
 background-color: #282828;
 border-right: 2px solid #49483e;
 border-left: 4px solid #282828;
}
div.cell.text_cell.unrendered .prompt {
 font-family: monospace, monospace;
 font-size: 9.5pt !important;
 font-weight: normal;
 color: #75715e !important;
 text-align: right !important;
 min-width: 14.5ex !important;
 width: 14.5ex !important;
 border-right: 2px solid #49483e;
 border-left: 4px solid #282828;
 background-color: #282828;
}
div.cell.text_cell.rendered .prompt {
 border-right: 2px solid #49483e;
}
div.cell.text_cell.rendered.selected .prompt {
 top: 0;
 border-left: 4px solid #57564b;
 border-right: 2px solid #49483e;
}
div.text_cell.unrendered.selected .prompt,
div.text_cell.rendered.selected .prompt {
 top: 0;
 background: #282828;
 border-left: 4px solid #33322b;
 border-right: 2px solid #49483e;
}
div.rendered_html code {
 font-family: monospace, monospace;
 font-size: 11pt;
 padding-top: 3px;
 padding-left: 2px;
 color: #f8f8f0;
 background: #282828;
 background-color: #282828;
}
pre,
code,
kbd,
samp {
 white-space: pre-wrap;
}
.well code,
code {
 font-family: monospace, monospace;
 font-size: 11pt !important;
 line-height: 170% !important;
 color: #f8f8f0;
 background: #282828;
 background-color: #282828;
 border-color: #282828;
}
kbd {
 padding: 1px;
 font-size: 11pt;
 font-weight: 800;
 color: #f8f8f0;
 background-color: transparent !important;
 border: 0;
 box-shadow: none;
}
pre {
 display: block;
 padding: 8.5px;
 margin: 0 0 9px;
 font-size: 12.0pt;
 line-height: 1.42857143;
 color: #f8f8f0;
 background-color: #282828;
 border: 1px solid #282828;
 border-radius: 2px;
}
div.rendered_html {
 color: #f8f8f0;
}
.rendered_html * + ul {
 margin-top: .4em;
 margin-bottom: .3em;
}
.rendered_html * + p {
 margin-top: .5em;
 margin-bottom: .5em;
}
div.rendered_html pre {
 font-family: monospace, monospace;
 font-size: 11pt !important;
 line-height: 170% !important;
 color: #f8f8f0 !important;
 background: #282828;
 background-color: #282828;
 max-width: 80%;
 border-radius: 0px;
 border-left: 3px solid #282828;
 max-width: 80%;
 border-radius: 0px;
 padding-left: 5px;
 margin-left: 6px;
}
div.text_cell_render pre,
div.text_cell_render code {
 font-family: monospace, monospace;
 font-size: 11pt !important;
 line-height: 170% !important;
 color: #f8f8f0;
 background: #1e1e1e;
 background-color: #1e1e1e;
 max-width: 80%;
 border-radius: 0px;
 border-left: none;
}
div.text_cell_render pre {
 border-left: 3px solid #49483e !important;
 max-width: 80%;
 border-radius: 0px;
 padding-left: 5px;
 margin-left: 6px;
}
div.text_cell_render h1,
div.rendered_html h1,
div.text_cell_render h2,
div.rendered_html h2,
div.text_cell_render h3,
div.rendered_html h3,
div.text_cell_render h4,
div.rendered_html h4,
div.text_cell_render h5,
div.rendered_html h5 {
 font-family: sans-serif;
 margin: 0.4em .2em .3em .2em !important;
}
.rendered_html h1:first-child,
.rendered_html h2:first-child,
.rendered_html h3:first-child,
.rendered_html h4:first-child,
.rendered_html h5:first-child,
.rendered_html h6:first-child {
 margin-top: 0.2em !important;
 margin-bottom: 0.2em !important;
}
.rendered_html h1,
.text_cell_render h1 {
 color: #a6e22e !important;
 font-size: 200%;
 text-align: left;
 font-style: normal;
 font-weight: normal;
}
.rendered_html h2,
.text_cell_render h2 {
 color: #a6e22e !important;
 font-size: 170%;
 font-style: normal;
 font-weight: normal;
}
.rendered_html h3,
.text_cell_render h3 {
 color: #a6e22e !important;
 font-size: 140%;
 font-style: normal;
 font-weight: normal;
}
.rendered_html h4,
.text_cell_render h4 {
 color: #a6e22e !important;
 font-size: 110%;
 font-style: normal;
 font-weight: normal;
}
.rendered_html h5,
.text_cell_render h5 {
 color: #a6e22e !important;
 font-size: 100%;
 font-style: normal;
 font-weight: normal;
}
hr {
 margin-top: 8px;
 margin-bottom: 10px;
 border: 0;
 border-top: 1px solid #a6e22e;
}
.rendered_html hr {
 color: #a6e22e;
 background-color: #a6e22e;
 margin-right: 2em;
}
#complete > select > option:hover {
 background: rgba(93,92,82,.25);
 background-color: rgba(93,92,82,.25);
}
div#_vivaldi-spatnav-focus-indicator._vivaldi-spatnav-focus-indicator {
 position: absolute;
 z-index: 9999999999;
 top: 0px;
 left: 0px;
 box-shadow: none;
 pointer-events: none;
 border-radius: 2px;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
 text-align: left;
 vertical-align: middle;
 padding: 0.42em 0.47em;
 line-height: normal;
 white-space: normal;
 max-width: none;
 border: none;
}
.rendered_html td {
 font-family: sans-serif !important;
 font-size: 9.3pt;
}
.rendered_html table {
 font-family: sans-serif !important;
 margin-left: 8px;
 margin-right: auto;
 border: none;
 border-collapse: collapse;
 border-spacing: 0;
 color: #cccccc;
 table-layout: fixed;
}
.rendered_html thead {
 font-family: sans-serif !important;
 font-size: 10.3pt !important;
 background: #1e1e1e;
 color: #cccccc;
 border-bottom: 1px solid #1e1e1e;
 vertical-align: bottom;
}
.rendered_html tbody tr:nth-child(odd) {
 background: #282828;
}
.rendered_html tbody tr {
 background: #202020;
}
.rendered_html tbody tr:hover:nth-child(odd) {
 background: #252525;
}
.rendered_html tbody tr:hover {
 background: #1e1e1e;
}
.rendered_html * + table {
 margin-top: .05em;
}
div.widget-area {
 background-color: #232323;
 background: #232323;
 color: #cccccc;
}
div.widget-area a {
 font-family: sans-serif;
 font-size: 12.0pt;
 font-weight: normal;
 font-style: normal;
 color: #f8f8f0;
 text-shadow: none !important;
}
div.widget-area a:hover,
div.widget-area a:focus {
 font-family: sans-serif;
 font-size: 12.0pt;
 font-weight: normal;
 font-style: normal;
 color: #f8f8f0;
 background: rgba(93,92,82,.25);
 background-color: rgba(93,92,82,.25);
 border-color: transparent;
 background-image: none;
 text-shadow: none !important;
}
div.widget_item.btn-group > button.btn.btn-default.widget-combo-btn,
div.widget_item.btn-group > button.btn.btn-default.widget-combo-btn:hover {
 background: #2c2c2c;
 background-color: #2c2c2c;
 border: 2px solid #2c2c2c !important;
 font-size: inherit;
 z-index: 0;
}
div.jupyter-widgets.widget-hprogress.widget-hbox {
 display: inline-table !important;
 width: 38% !important;
 margin-left: 10px;
}
div.jupyter-widgets.widget-hprogress.widget-hbox .widget-label,
div.widget-hbox .widget-label,
.widget-hbox .widget-label,
.widget-inline-hbox .widget-label,
div.widget-label {
 text-align: -webkit-auto !important;
 margin-left: 15px !important;
 max-width: 240px !important;
 min-width: 100px !important;
 vertical-align: text-top !important;
 color: #cccccc !important;
 font-size: 14px !important;
}
.widget-hprogress .progress {
 flex-grow: 1;
 height: 20px;
 margin-top: auto;
 margin-left: 12px;
 margin-bottom: auto;
 width: 300px;
}
.progress {
 overflow: hidden;
 height: 22px;
 margin-bottom: 10px;
 padding-left: 10px;
 background-color: #49483e !important;
 border-radius: 2px;
 -webkit-box-shadow: none;
 box-shadow: none;
 z-index: 10;
}
.progress-bar-danger {
 background-color: #e74c3c !important;
}
.progress-bar-info {
 background-color: #3498db !important;
}
.progress-bar-warning {
 background-color: #ff914d !important;
}
.progress-bar-success {
 background-color: #83a83b !important;
}
.widget-select select {
 margin-left: 12px;
}
.rendered_html :link {
 font-family: sans-serif;
 font-size: 100%;
 color: #a6e22e;
 text-decoration: underline;
}
.rendered_html :visited,
.rendered_html :visited:active,
.rendered_html :visited:focus {
 color: #acdf45;
}
.rendered_html :visited:hover,
.rendered_html :link:hover {
 font-family: sans-serif;
 font-size: 100%;
 color: #97dc0b;
}
div.cell.text_cell a.anchor-link:link {
 font-size: inherit;
 text-decoration: none;
 padding: 0px 20px;
 visibility: none;
 color: rgba(0,0,0,.32);
}
div.cell.text_cell a.anchor-link:link:hover {
 font-size: inherit;
 color: #a6e22e;
}
.navbar-text {
 margin-top: 4px;
 margin-bottom: 0px;
}
#clusters > a {
 color: #a6e22e;
 text-decoration: underline;
 cursor: auto;
}
#clusters > a:hover {
 color: #ae81ff;
 text-decoration: underline;
 cursor: auto;
}
#nbextensions-configurator-container > div.row.container-fluid.nbext-selector > h3 {
 font-size: 17px;
 margin-top: 5px;
 margin-bottom: 8px;
 height: 24px;
 padding: 4px 0 4px 0;
}
div#nbextensions-configurator-container.container,
#nbextensions-configurator-container.container {
 width: 100%;
 margin-right: auto;
 margin-left: auto;
}
div.nbext-selector > nav > .nav > li > a {
 font-family: sans-serif;
 font-size: 10.5pt;
 padding: 2px 5px;
}
div.nbext-selector > nav > .nav > li > a:hover {
 background: transparent;
}
div.nbext-selector > nav > .nav > li:hover {
 background-color: rgba(93,92,82,.25) !important;
 background: rgba(93,92,82,.25) !important;
}
div.nbext-selector > nav > .nav > li.active:hover {
 background: transparent !important;
 background-color: transparent !important;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:active,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
 color: #f8f8f2;
 background-color: rgba(93,92,82,.25) !important;
 background: rgba(93,92,82,.25) !important;
 -webkit-backface-visibility: hidden;
 -webkit-font-smoothing: subpixel-antialiased !important;
}
div.nbext-readme > .nbext-readme-contents > .rendered_html {
 font-family: sans-serif;
 font-size: 11.5pt;
 line-height: 145%;
 padding: 1em 1em;
 color: #f8f8f0;
 background-color: #282828;
 -webkit-box-shadow: none;
 -moz-box-shadow: none;
 box-shadow: none;
}
.nbext-icon,
.nbext-desc,
.nbext-compat-div,
.nbext-enable-btns,
.nbext-params {
 margin-bottom: 8px;
 font-size: 11.5pt;
}
div.nbext-readme > .nbext-readme-contents {
 padding: 0;
 overflow-y: hidden;
}
div.nbext-readme > .nbext-readme-contents:not(:empty) {
 margin-top: 0.5em;
 margin-bottom: 2em;
 border: none;
 border-top-color: rgba(148,204,114,.2);
}
.nbext-showhide-incompat {
 padding-bottom: 0.5em;
 color: #888888;
 font-size: 10.5pt;
}
.nbext-filter-menu.dropdown-menu > li > a:hover,
.nbext-filter-menu.dropdown-menu > li > a:focus,
.nbext-filter-menu.dropdown-menu > li > a.ui-state-focus {
 color: #f8f8f0 !important;
 background-color: rgba(93,92,82,.25) !important;
 background: rgba(93,92,82,.25) !important;
 border-color: rgba(93,92,82,.25) !important;
}
.nbext-filter-input-wrap > .nbext-filter-input-subwrap,
.nbext-filter-input-wrap > .nbext-filter-input-subwrap > input {
 border: none;
 outline: none;
 background-color: transparent;
 padding: 0;
 vertical-align: middle;
 margin-top: -2px;
}
span.rendered_html code {
 background-color: transparent;
 color: #f8f8f0;
}
#nbextensions-configurator-container > div.row.container-fluid.nbext-selector {
 padding-left: 0px;
 padding-right: 0px;
}
.nbext-filter-menu {
 max-height: 55vh !important;
 overflow-y: auto;
 outline: none;
 border: none;
}
.nbext-filter-menu:hover {
 border: none;
}
.alert-warning {
 background-color: #232323;
 border-color: #232323;
 color: #f8f8f0;
}
.notification_widget.danger {
 color: #ffffff;
 background-color: #e74c3c;
 border-color: #e74c3c;
 padding-right: 5px;
}
#nbextensions-configurator-container > div.nbext-buttons.tree-buttons.no-padding.pull-right > span > button {
 border: none !important;
}
button#refresh_running_list {
 border: none !important;
}
mark,
.mark {
 background-color: #282828;
 color: #f8f8f0;
 padding: .15em;
}
a.text-warning,
a.text-warning:hover {
 color: #75715e;
}
a.text-warning.bg-warning {
 background-color: #1e1e1e;
}
span.bg-success.text-success {
 background-color: transparent;
 color: #a6e22e;
}
span.bg-danger.text-danger {
 background-color: #1e1e1e;
 color: #f92672;
}
.has-success .input-group-addon {
 color: #a6e22e;
 border-color: transparent;
 background: inherit;
 background-color: rgba(83,180,115,.10);
}
.has-success .form-control {
 border-color: #a6e22e;
 -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,0.025);
 box-shadow: inset 0 1px 1px rgba(0,0,0,0.025);
}
.has-error .input-group-addon {
 color: #f92672;
 border-color: transparent;
 background: inherit;
 background-color: rgba(192,57,67,.10);
}
.has-error .form-control {
 border-color: #f92672;
 -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,0.025);
 box-shadow: inset 0 1px 1px rgba(0,0,0,0.025);
}
.kse-input-group-pretty > kbd {
 font-family: monospace, monospace;
 color: #f8f8f0;
 font-weight: normal;
 background: transparent;
}
.kse-input-group-pretty > kbd {
 font-family: monospace, monospace;
 color: #f8f8f0;
 font-weight: normal;
 background: transparent;
}
div.nbext-enable-btns .btn[disabled],
div.nbext-enable-btns .btn[disabled]:hover,
.btn-default.disabled,
.btn-default[disabled] {
 background: #2c2c2c;
 background-color: #2c2c2c;
 color: #f3f3e6;
}
label#Keyword-Filter {
 display: none;
}
.input-group .nbext-list-btn-add,
.input-group-btn:last-child > .btn-group > .btn {
 background: #2f2f2f;
 background-color: #2f2f2f;
 border-color: #2f2f2f;
 border: 2px solid #2f2f2f;
}
.input-group .nbext-list-btn-add:hover,
.input-group-btn:last-child > .btn-group > .btn:hover {
 background: #2a2a2a;
 background-color: #2a2a2a;
 border-color: #2a2a2a;
 border: 2px solid #2a2a2a;
}
#notebook-container > div.cell.code_cell.rendered.selected > div.widget-area > div.widget-subarea > div > div.widget_item.btn-group > button.btn.btn-default.dropdown-toggle.widget-combo-carrot-btn {
 background: #2f2f2f;
 background-color: #2f2f2f;
 border-color: #2f2f2f;
}
#notebook-container > div.cell.code_cell.rendered.selected > div.widget-area > div.widget-subarea > div > div.widget_item.btn-group > button.btn.btn-default.dropdown-toggle.widget-combo-carrot-btn:hover {
 background: #2a2a2a;
 background-color: #2a2a2a;
 border-color: #2a2a2a;
}
.ui-widget-content {
 background: #2f2f2f;
 background-color: #2f2f2f;
 border: 2px solid #2f2f2f;
 color: #f8f8f0;
}
div.collapsible_headings_toggle {
 color: rgba(93,92,82,.5) !important;
}
div.collapsible_headings_toggle:hover {
 color: #a6e22e !important;
}
.collapsible_headings_toggle .h1,
.collapsible_headings_toggle .h2,
.collapsible_headings_toggle .h3,
.collapsible_headings_toggle .h4,
.collapsible_headings_toggle .h5,
.collapsible_headings_toggle .h6 {
 margin: 0.3em .4em 0em 0em !important;
 line-height: 1.2 !important;
}
div.collapsible_headings_toggle .fa-caret-down:before,
div.collapsible_headings_toggle .fa-caret-right:before {
 font-size: xx-large;
 transition: transform 1000ms;
 transform: none !important;
}
.collapsible_headings_collapsed.collapsible_headings_ellipsis .rendered_html h1:after,
.collapsible_headings_collapsed.collapsible_headings_ellipsis .rendered_html h2:after,
.collapsible_headings_collapsed.collapsible_headings_ellipsis .rendered_html h3:after,
.collapsible_headings_collapsed.collapsible_headings_ellipsis .rendered_html h4:after,
.collapsible_headings_collapsed.collapsible_headings_ellipsis .rendered_html h5:after,
.collapsible_headings_collapsed.collapsible_headings_ellipsis .rendered_html h6:after {
 position: absolute;
 right: 0;
 bottom: 20% !important;
 content: "[\002026]";
 color: rgba(93,92,82,.5) !important;
 padding: 0.5em 0em 0em 0em !important;
}
.collapsible_headings_ellipsis .rendered_html h1,
.collapsible_headings_ellipsis .rendered_html h2,
.collapsible_headings_ellipsis .rendered_html h3,
.collapsible_headings_ellipsis .rendered_html h4,
.collapsible_headings_ellipsis .rendered_html h5,
.collapsible_headings_ellipsis .rendered_html h6,
.collapsible_headings_toggle .fa {
 transition: transform 1000ms !important;
 -webkit-transform: inherit !important;
 -moz-transform: inherit !important;
 -ms-transform: inherit !important;
 -o-transform: inherit !important;
 transform: inherit !important;
 padding-right: 0px !important;
}
#toc-wrapper {
 z-index: 90;
 position: fixed !important;
 display: flex;
 flex-direction: column;
 overflow: hidden;
 padding: 10px;
 border-style: solid;
 border-width: thin;
 border-right-width: medium !important;
 background-color: #1e1e1e !important;
}
#toc-wrapper.ui-draggable.ui-resizable.sidebar-wrapper {
 border-color: rgba(93,92,82,.25) !important;
}
#toc a,
#navigate_menu a,
.toc {
 color: #f8f8f0 !important;
 font-size: 11pt !important;
}
#toc li > span:hover {
 background-color: rgba(93,92,82,.25) !important;
}
#toc a:hover,
#navigate_menu a:hover,
.toc {
 color: #f8f8f2 !important;
 font-size: 11pt !important;
}
#toc-wrapper .toc-item-num {
 color: #a6e22e !important;
 font-size: 11pt !important;
}
input.raw_input {
 font-family: monospace, monospace;
 font-size: 11pt !important;
 color: #f8f8f0;
 background-color: #282828;
 border-color: #252525;
 background: #252525;
 width: auto;
 vertical-align: baseline;
 padding: 0em 0.25em;
 margin: 0em 0.25em;
 -webkit-box-shadow: none;
 box-shadow: none;
}
audio,
video {
 display: inline;
 vertical-align: middle;
 align-content: center;
 margin-left: 20%;
}
.cmd-palette .modal-body {
 padding: 0px;
 margin: 0px;
}
.cmd-palette form {
 background: #293547;
 background-color: #293547;
}
.typeahead-field input:last-child,
.typeahead-hint {
 background: #293547;
 background-color: #293547;
 z-index: 1;
}
.typeahead-field input {
 font-family: sans-serif;
 color: #f8f8f0;
 border: none;
 font-size: 28pt;
 display: inline-block;
 line-height: inherit;
 padding: 3px 10px;
 height: 70px;
}
.typeahead-select {
 background-color: #293547;
}
body > div.modal.cmd-palette.typeahead-field {
 display: table;
 border-collapse: separate;
 background-color: #2b3850;
}
.typeahead-container button {
 font-family: sans-serif;
 font-size: 28pt;
 background-color: #2f2f2f;
 border: none;
 display: inline-block;
 line-height: inherit;
 padding: 3px 10px;
 height: 70px;
}
.typeahead-search-icon {
 min-width: 40px;
 min-height: 55px;
 display: block;
 vertical-align: middle;
 text-align: center;
}
.typeahead-container button:focus,
.typeahead-container button:hover {
 color: #f8f8f0;
 background-color: #2a2a2a;
 border-color: #2a2a2a;
}
.typeahead-list > li.typeahead-group.active > a,
.typeahead-list > li.typeahead-group > a,
.typeahead-list > li.typeahead-group > a:focus,
.typeahead-list > li.typeahead-group > a:hover {
 display: none;
}
.typeahead-dropdown > li > a,
.typeahead-list > li > a {
 color: #f8f8f0;
 text-decoration: none;
}
.typeahead-dropdown,
.typeahead-list {
 font-family: sans-serif;
 font-size: 13pt;
 color: #f8f8f0;
 background-color: #202937;
 border: none;
 background-clip: padding-box;
 margin-top: 0px;
 padding: 3px 2px 3px 0px;
 line-height: 1.7;
}
.typeahead-dropdown > li.active > a,
.typeahead-dropdown > li > a:focus,
.typeahead-dropdown > li > a:hover,
.typeahead-list > li.active > a,
.typeahead-list > li > a:focus,
.typeahead-list > li > a:hover {
 color: #f8f8f0;
 background-color: #2b3850;
 border-color: #2b3850;
}
.command-shortcut:before {
 content: "(command)";
 padding-right: 3px;
 color: #75715e;
}
.edit-shortcut:before {
 content: "(edit)";
 padding-right: 3px;
 color: #75715e;
}
ul.typeahead-list i {
 margin-left: 1px;
 width: 18px;
 margin-right: 10px;
}
ul.typeahead-list {
 max-height: 50vh;
 overflow: auto;
}
.typeahead-list > li {
 position: relative;
 border: none;
}
div.input.typeahead-hint,
input.typeahead-hint,
body > div.modal.cmd-palette.in > div > div > div > form > div > div.typeahead-field > span.typeahead-query > input.typeahead-hint {
 color: #75715e !important;
 background-color: transparent;
 padding: 3px 10px;
}
.typeahead-dropdown > li > a,
.typeahead-list > li > a {
 display: block;
 padding: 5px;
 clear: both;
 font-weight: 400;
 line-height: 1.7;
 border: 1px solid #202937;
 border-bottom-color: rgba(93,92,82,.5);
}
body > div.modal.cmd-palette.in > div {
 min-width: 750px;
 margin: 150px auto;
}
.typeahead-container strong {
 font-weight: bolder;
 color: #a6e22e;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
 color: #ffffff;
 background-color: #57564b;
 border-color: #57564b;
 border-style: solid;
 border-width: 1px;
 border-radius: 0px;
}
#find-and-replace #replace-preview .replace .match {
 background-color: #f92672;
 border-color: #f92672;
 border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
 background-color: #a6e22e;
 border-color: #a6e22e;
 border-radius: 0px;
}
.jupyter-dashboard-menu-item.selected::before {
 font-family: 'FontAwesome' !important;
 content: '\f00c' !important;
 position: absolute !important;
 color: #a6e22e !important;
 left: 0px !important;
 top: 13px !important;
 font-size: 12px !important;
}
.shortcut_key,
span.shortcut_key {
 display: inline-block;
 width: 16ex;
 text-align: right;
 font-family: monospace;
}
.jupyter-keybindings {
 padding: 1px;
 line-height: 24px;
 border-bottom: 1px solid rgba(93,92,82,.25);
}
.jupyter-keybindings i {
 background: #282828;
 font-size: small;
 padding: 5px;
 margin-left: 7px;
}
div#short-key-bindings-intro.well,
.well {
 background-color: #2f2f2f;
 border: 1px solid #2f2f2f;
 color: #f8f8f0;
 border-radius: 2px;
 -webkit-box-shadow: none;
 box-shadow: none;
}
#texteditor-backdrop {
 background: #1e1e1e;
 background-color: #1e1e1e;
}
#texteditor-backdrop #texteditor-container .CodeMirror-gutter,
#texteditor-backdrop #texteditor-container .CodeMirror-gutters {
 background: #49483e;
 background-color: #49483e;
 color: #75715e;
}
.edit_app #menubar .navbar {
 margin-bottom: 0px;
}
#texteditor-backdrop #texteditor-container {
 padding: 0px;
 background-color: #282828;
 box-shadow: none;
}
.terminal-app {
 background: #1e1e1e;
}
.terminal-app > #header {
 background: #1e1e1e;
}
.terminal-app .terminal {
 font-family: monospace, monospace;
 font-size: 11pt;
 line-height: 170%;
 color: #f8f8f0;
 background: #282828;
 padding: 0.4em;
 border-radius: 2px;
 -webkit-box-shadow: none;
 box-shadow: none;
}
.terminal .xterm-viewport {
 background-color: #282828;
 color: #f8f8f0;
 overflow-y: auto;
}
.terminal .xterm-color-0 {
 color: #a6e22e;
}
.terminal .xterm-color-1 {
 color: #a6e22e;
}
.terminal .xterm-color-2 {
 color: #f92672;
}
.terminal .xterm-color-3 {
 color: #a6e22e;
}
.terminal .xterm-color-4 {
 color: #ae81ff;
}
.terminal .xterm-color-5 {
 color: #e6db74;
}
.terminal .xterm-color-6 {
 color: #a6e22e;
}
.terminal .xterm-color-7 {
 color: #a6e22e;
}
.terminal .xterm-color-8 {
 color: #a6e22e;
}
.terminal .xterm-color-9 {
 color: #e6db74;
}
.terminal .xterm-color-10 {
 color: #a6e22e;
}
.terminal .xterm-color-14 {
 color: #a6e22e;
}
.terminal .xterm-bg-color-15 {
 background-color: #282828;
}
.terminal:not(.xterm-cursor-style-underline):not(.xterm-cursor-style-bar) .terminal-cursor {
 background-color: #a6e22e;
 color: #282828;
}
.terminal:not(.focus) .terminal-cursor {
 outline: 1px solid #a6e22e;
 outline-offset: -1px;
}
.celltoolbar {
 font-size: 100%;
 padding-top: 3px;
 border-color: transparent;
 border-bottom: thin solid rgba(148,204,114,.2);
 background: transparent;
}
.cell-tag,
.tags-input input,
.tags-input button {
 color: #f8f8f0;
 background-color: #1e1e1e;
 background-image: none;
 border: 1px solid #f8f8f0;
 border-radius: 1px;
 box-shadow: none;
 width: inherit;
 font-size: inherit;
 height: 22px;
 line-height: 22px;
}
#notebook-container > div.cell.code_cell.rendered.selected > div.input > div.inner_cell > div.ctb_hideshow.ctb_show > div > div > button,
#notebook-container > div.input > div.inner_cell > div.ctb_hideshow.ctb_show > div > div > button {
 font-size: 10pt;
 color: #f8f8f0;
 background-color: #1e1e1e;
 background-image: none;
 border: 1px solid #f8f8f0;
 border-radius: 1px;
 box-shadow: none;
 width: inherit;
 font-size: inherit;
 height: 22px;
 line-height: 22px;
}
div#pager #pager-contents {
 background: #1e1e1e !important;
 background-color: #1e1e1e !important;
}
div#pager pre {
 color: #f8f8f0 !important;
 background: #282828 !important;
 background-color: #282828 !important;
 padding: 0.4em;
}
div#pager .ui-resizable-handle {
 top: 0px;
 height: 8px;
 background: #a6e22e !important;
 border-top: 1px solid #a6e22e;
 border-bottom: 1px solid #a6e22e;
}
div.CodeMirror,
div.CodeMirror pre {
 font-family: monospace, monospace;
 font-size: 11pt;
 line-height: 170%;
 color: #f8f8f0;
}
div.CodeMirror-lines {
 padding-bottom: .9em;
 padding-left: .5em;
 padding-right: 1.5em;
 padding-top: .7em;
}
span.ansiblack,
.ansi-black-fg {
 color: #282828;
}
span.ansiblue,
.ansi-blue-fg,
.ansi-blue-intense-fg {
 color: #66d9ef;
}
span.ansigray,
.ansi-gray-fg,
.ansi-gray-intense-fg {
 color: #888888;
}
span.ansigreen,
.ansi-green-fg {
 color: #a6e22e;
}
.ansi-green-intense-fg {
 color: #888888;
}
span.ansipurple,
.ansi-purple-fg,
.ansi-purple-intense-fg {
 color: #ae81ff;
}
span.ansicyan,
.ansi-cyan-fg,
.ansi-cyan-intense-fg {
 color: #ae81ff;
}
span.ansiyellow,
.ansi-yellow-fg,
.ansi-yellow-intense-fg {
 color: #e6db74;
}
span.ansired,
.ansi-red-fg,
.ansi-red-intense-fg {
 color: #f92672;
}
div.output-stderr {
 background-color: #f92672;
}
div.output-stderr pre {
 color: #f8f8f2;
}
div.js-error {
 color: #f92672;
}
.ipython_tooltip {
 font-family: monospace, monospace;
 font-size: 11pt;
 line-height: 170%;
 border: 2px solid #141414;
 background: #282828;
 background-color: #282828;
 border-radius: 2px;
 overflow-x: visible;
 overflow-y: visible;
 box-shadow: none;
 position: absolute;
 z-index: 1000;
}
.ipython_tooltip .tooltiptext pre {
 font-family: monospace, monospace;
 font-size: 11pt;
 line-height: 170%;
 background: #282828;
 background-color: #282828;
 color: #f8f8f0;
 overflow-x: visible;
 overflow-y: visible;
 max-width: 900px;
}
div#tooltip.ipython_tooltip {
 overflow-x: wrap;
 overflow-y: visible;
 max-width: 800px;
}
div.tooltiptext.bigtooltip {
 overflow-x: visible;
 overflow-y: scroll;
 height: 400px;
 max-width: 800px;
}
.cm-s-ipython.CodeMirror {
 font-family: monospace, monospace;
 font-size: 11pt;
 background: #282828;
 color: #f8f8f0;
 border-radius: 2px;
 font-style: normal;
 font-weight: normal;
}
.cm-s-ipython div.CodeMirror-selected {
 background: #49483e;
}
.CodeMirror-gutters {
 border: none;
 border-right: 1px solid #49483e !important;
 background-color: #49483e !important;
 background: #49483e !important;
 border-radius: 0px;
 white-space: nowrap;
}
.cm-s-ipython .CodeMirror-gutters {
 background: #49483e;
 border: none;
 border-radius: 0px;
 width: 36px;
}
.cm-s-ipython .CodeMirror-linenumber {
 color: #75715e;
}
.CodeMirror-sizer {
 margin-left: 40px;
}
.CodeMirror-linenumber,
div.CodeMirror-linenumber,
.CodeMirror-gutter.CodeMirror-linenumberdiv.CodeMirror-gutter.CodeMirror-linenumber {
 padding-right: 1px;
 margin-left: 0px;
 margin: 0px;
 width: 26px !important;
 padding: 0px;
 text-align: right;
}
.CodeMirror-linenumber {
 color: #75715e;
}
.cm-s-ipython .CodeMirror-cursor {
 border-left: 2px solid #0095ff !important;
}
.cm-s-ipython span.cm-comment {
 color: #75715e;
 font-style: italic;
}
.cm-s-ipython span.cm-atom {
 color: #ae81ff;
}
.cm-s-ipython span.cm-number {
 color: #ae81ff;
}
.cm-s-ipython span.cm-property {
 color: #f8f8f0;
}
.cm-s-ipython span.cm-attribute {
 color: #f8f8f0;
}
.cm-s-ipython span.cm-keyword {
 color: #f92672;
 font-weight: normal;
}
.cm-s-ipython span.cm-string {
 color: #e6db74;
}
.cm-s-ipython span.cm-meta {
 color: #fd971f;
}
.cm-s-ipython span.cm-operator {
 color: #a6e22e;
}
.cm-s-ipython span.cm-builtin {
 color: #a6e22e;
}
.cm-s-ipython span.cm-variable {
 color: #f8f8f0;
}
.cm-s-ipython span.cm-variable-2 {
 color: #a6e22e;
}
.cm-s-ipython span.cm-variable-3 {
 color: #fd971f;
}
.cm-s-ipython span.cm-def {
 color: #a6e22e;
 font-weight: normal;
}
.cm-s-ipython span.cm-error {
 background: rgba(249,38,114,.4);
}
.cm-s-ipython span.cm-tag {
 color: #ae81ff;
}
.cm-s-ipython span.cm-link {
 color: #a6e22e;
}
.cm-s-ipython span.cm-storage {
 color: #ae81ff;
}
.cm-s-ipython span.cm-entity {
 color: #a6e22e;
}
.cm-s-ipython span.cm-quote {
 color: #e6db74;
}
div.CodeMirror span.CodeMirror-matchingbracket {
 color: #ffffff;
 font-weight: bold;
 background-color: #49483e;
}
div.CodeMirror span.CodeMirror-nonmatchingbracket {
 color: #ffffff;
 font-weight: bold;
 background: rgba(249,38,114,.4) !important;
}
.cm-header-1 {
 font-size: 215%;
}
.cm-header-2 {
 font-size: 180%;
}
.cm-header-3 {
 font-size: 150%;
}
.cm-header-4 {
 font-size: 120%;
}
.cm-header-5 {
 font-size: 100%;
}
.cm-s-default .cm-hr {
 color: #a6e22e;
}
div.cell.text_cell .cm-s-default .cm-header {
 font-family: sans-serif;
 font-weight: normal;
 color: #a6e22e !important;
 margin-top: 0.3em !important;
 margin-bottom: 0.3em !important;
}
div.cell.text_cell .cm-s-default span.cm-variable-2 {
 color: #f8f8f0 !important;
}
div.cell.text_cell .cm-s-default span.cm-variable-3 {
 color: #fd971f !important;
}
.cm-s-default span.cm-comment {
 color: #75715e !important;
}
.cm-s-default .cm-tag {
 color: #529b2f;
}
.cm-s-default .cm-builtin {
 color: #a6e22e;
}
.cm-s-default .cm-string {
 color: #e6db74;
}
.cm-s-default .cm-keyword {
 color: #f92672;
}
.cm-s-default .cm-number {
 color: #ae81ff;
}
.cm-s-default .cm-error {
 color: #ae81ff;
}
.cm-s-default .cm-link {
 color: #a6e22e;
}
.cm-s-default .cm-atom {
 color: #ae81ff;
}
.cm-s-default .cm-def {
 color: #a6e22e;
}
.CodeMirror-cursor {
 border-left: 2px solid #0095ff !important;
 border-right: none;
 width: 0;
}
.cm-s-default div.CodeMirror-selected {
 background: #49483e;
}
.cm-s-default .cm-selected {
 background: #49483e;
}
.MathJax_Display,
.MathJax {
 border: 0 !important;
 font-size: 100% !important;
 text-align: center !important;
 margin: 0em !important;
 line-height: 2.25 !important;
}
.MathJax:focus,
body :focus .MathJax {
 display: inline-block !important;
}
.MathJax:focus,
body :focus .MathJax {
 display: inline-block !important;
}
.completions {
 position: absolute;
 z-index: 110;
 overflow: hidden;
 border: medium solid #49483e;
 box-shadow: none;
 line-height: 1;
}
.completions select {
 background: #282828;
 background-color: #282828;
 outline: none;
 border: none;
 padding: 0px;
 margin: 0px;
 margin-left: 2px;
 overflow: auto;
 font-family: monospace, monospace;
 font-size: 11pt;
 color: #f8f8f0;
 width: auto;
}
div#maintoolbar {
 display: none !important;
}
#header-container {
 display: none !important;
}

<script>
    MathJax.Hub.Config({
        "HTML-CSS": {
            /*preferredFont: "TeX",*/
            /*availableFonts: ["TeX", "STIX"],*/
            styles: {
                scale: 100,
                ".MathJax_Display": {
                    "font-size": "100%",
                }
            }
        }
    });
</script>
     </style>




```python
data1 = {
    'name': ['NameA', 'NameB', 'NameC', 'NameD', 'NameA'],
    'age': [20, 21, 22, 23, 24],
    'addr': ['CityA', 'CityB', 'CityC', 'CityD', 'CityA'],
    'qualification': ['MSc', 'BBA', 'BE', 'Bcom', 'MSc'],
    'salary' : [100, 150, 2000, 250, 300]
}
```


```python

```


```python
data1
```




    {'name': ['NameA', 'NameB', 'NameC', 'NameD', 'NameA'],
     'age': [20, 21, 22, 23, 24],
     'addr': ['CityA', 'CityB', 'CityC', 'CityD', 'CityA'],
     'qualification': ['MSc', 'BBA', 'BE', 'Bcom', 'MSc'],
     'salary': [100, 150, 2000, 250, 300]}




```python
df1 = pd.DataFrame(data1)
```


```python
df1
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
      <th>name</th>
      <th>age</th>
      <th>addr</th>
      <th>qualification</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NameA</td>
      <td>20</td>
      <td>CityA</td>
      <td>MSc</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NameB</td>
      <td>21</td>
      <td>CityB</td>
      <td>BBA</td>
      <td>150</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NameC</td>
      <td>22</td>
      <td>CityC</td>
      <td>BE</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NameD</td>
      <td>23</td>
      <td>CityD</td>
      <td>Bcom</td>
      <td>250</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NameA</td>
      <td>24</td>
      <td>CityA</td>
      <td>MSc</td>
      <td>300</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.groupby('name')
df1.groupby('name').groups
```




    {'NameA': [0, 4], 'NameB': [1], 'NameC': [2], 'NameD': [3]}




```python
df1.groupby('qualification').groups
```




    {'BBA': [1], 'BE': [2], 'Bcom': [3], 'MSc': [0, 4]}




```python
# print groups with multiple columns
df1.groupby(['qualification', 'name']).groups
```




    {('BBA', 'NameB'): [1], ('BE', 'NameC'): [2], ('Bcom', 'NameD'): [3], ('MSc', 'NameA'): [0, 4]}




```python
# iterate over groups
map = df1.groupby(['qualification', 'name']).groups
for k in map:
    print(k, '->',map[k])
```

    ('BBA', 'NameB') -> Int64Index([1], dtype='int64')
    ('BE', 'NameC') -> Int64Index([2], dtype='int64')
    ('Bcom', 'NameD') -> Int64Index([3], dtype='int64')
    ('MSc', 'NameA') -> Int64Index([0, 4], dtype='int64')
    


```python
# groupby and sum
df1.groupby(['name','age','salary']).sum()
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
      <th></th>
      <th></th>
      <th>addr</th>
      <th>qualification</th>
    </tr>
    <tr>
      <th>name</th>
      <th>age</th>
      <th>salary</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">NameA</th>
      <th>20</th>
      <th>100</th>
      <td>CityA</td>
      <td>MSc</td>
    </tr>
    <tr>
      <th>24</th>
      <th>300</th>
      <td>CityA</td>
      <td>MSc</td>
    </tr>
    <tr>
      <th>NameB</th>
      <th>21</th>
      <th>150</th>
      <td>CityB</td>
      <td>BBA</td>
    </tr>
    <tr>
      <th>NameC</th>
      <th>22</th>
      <th>2000</th>
      <td>CityC</td>
      <td>BE</td>
    </tr>
    <tr>
      <th>NameD</th>
      <th>23</th>
      <th>250</th>
      <td>CityD</td>
      <td>Bcom</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.groupby(['name','age','salary']).sum()
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
      <th></th>
      <th></th>
      <th>addr</th>
      <th>qualification</th>
    </tr>
    <tr>
      <th>name</th>
      <th>age</th>
      <th>salary</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">NameA</th>
      <th>20</th>
      <th>100</th>
      <td>CityA</td>
      <td>MSc</td>
    </tr>
    <tr>
      <th>24</th>
      <th>300</th>
      <td>CityA</td>
      <td>MSc</td>
    </tr>
    <tr>
      <th>NameB</th>
      <th>21</th>
      <th>150</th>
      <td>CityB</td>
      <td>BBA</td>
    </tr>
    <tr>
      <th>NameC</th>
      <th>22</th>
      <th>2000</th>
      <td>CityC</td>
      <td>BE</td>
    </tr>
    <tr>
      <th>NameD</th>
      <th>23</th>
      <th>250</th>
      <td>CityD</td>
      <td>Bcom</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.groupby(['addr']).sum()
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
      <th>age</th>
      <th>salary</th>
    </tr>
    <tr>
      <th>addr</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>CityA</th>
      <td>44</td>
      <td>400</td>
    </tr>
    <tr>
      <th>CityB</th>
      <td>21</td>
      <td>150</td>
    </tr>
    <tr>
      <th>CityC</th>
      <td>22</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>CityD</th>
      <td>23</td>
      <td>250</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.groupby(['qualification']).sum()
df1.groupby(['qualification']).sum().sort_values('salary')
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
      <th>age</th>
      <th>salary</th>
    </tr>
    <tr>
      <th>qualification</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>BBA</th>
      <td>21</td>
      <td>150</td>
    </tr>
    <tr>
      <th>Bcom</th>
      <td>23</td>
      <td>250</td>
    </tr>
    <tr>
      <th>MSc</th>
      <td>44</td>
      <td>400</td>
    </tr>
    <tr>
      <th>BE</th>
      <td>22</td>
      <td>2000</td>
    </tr>
  </tbody>
</table>
</div>




```python
dataA = {
    'name': ['NameA', 'NameB'],
    'age': [20, 21],
    'addr': ['CityA', 'CityB'],
    'qualification': ['MSc', 'BBA'],
    'salary' : [100, 150]
}
```


```python
dataB = {
    'name': ['NameC', 'NameD', 'NameA'],
    'age': [22, 23, 24],
    'addr': ['CityC', 'CityD', 'CityA'],
    'qualification': ['BE', 'Bcom', 'MSc'],
    'salary' : [2000, 250, 300]
}
```


```python
dfA = pd.DataFrame(dataA, index=[0,1])
dfB = pd.DataFrame(dataB, index=[2,3,4])
```


```python
# merge 2 data frames
```


```python
dfC = pd.concat([dfA, dfB])
dfC
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
      <th>name</th>
      <th>age</th>
      <th>addr</th>
      <th>qualification</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NameA</td>
      <td>20</td>
      <td>CityA</td>
      <td>MSc</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NameB</td>
      <td>21</td>
      <td>CityB</td>
      <td>BBA</td>
      <td>150</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NameC</td>
      <td>22</td>
      <td>CityC</td>
      <td>BE</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NameD</td>
      <td>23</td>
      <td>CityD</td>
      <td>Bcom</td>
      <td>250</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NameA</td>
      <td>24</td>
      <td>CityA</td>
      <td>MSc</td>
      <td>300</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfA = pd.DataFrame(dataA)
dfB = pd.DataFrame(dataB)
```


```python
dfA
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
      <th>name</th>
      <th>age</th>
      <th>addr</th>
      <th>qualification</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NameA</td>
      <td>20</td>
      <td>CityA</td>
      <td>MSc</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NameB</td>
      <td>21</td>
      <td>CityB</td>
      <td>BBA</td>
      <td>150</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfB
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
      <th>name</th>
      <th>age</th>
      <th>addr</th>
      <th>qualification</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NameC</td>
      <td>22</td>
      <td>CityC</td>
      <td>BE</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NameD</td>
      <td>23</td>
      <td>CityD</td>
      <td>Bcom</td>
      <td>250</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NameA</td>
      <td>24</td>
      <td>CityA</td>
      <td>MSc</td>
      <td>300</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfC=pd.concat([dfA, dfB])
```


```python
dfC
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
      <th>name</th>
      <th>age</th>
      <th>addr</th>
      <th>qualification</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NameA</td>
      <td>20</td>
      <td>CityA</td>
      <td>MSc</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NameB</td>
      <td>21</td>
      <td>CityB</td>
      <td>BBA</td>
      <td>150</td>
    </tr>
    <tr>
      <th>0</th>
      <td>NameC</td>
      <td>22</td>
      <td>CityC</td>
      <td>BE</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NameD</td>
      <td>23</td>
      <td>CityD</td>
      <td>Bcom</td>
      <td>250</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NameA</td>
      <td>24</td>
      <td>CityA</td>
      <td>MSc</td>
      <td>300</td>
    </tr>
  </tbody>
</table>
</div>




```python
# to avoid duplicate indexing, we have to provide index while creating dataFrame
# so while merging we can see the user provided index, instead of sys generated
```


```python
df
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
      <th>PassengerIndex</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>886</th>
      <td>887</td>
      <td>0</td>
      <td>2</td>
      <td>Montvila, Rev. Juozas</td>
      <td>male</td>
      <td>27.0</td>
      <td>0</td>
      <td>0</td>
      <td>211536</td>
      <td>13.0000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>887</th>
      <td>888</td>
      <td>1</td>
      <td>1</td>
      <td>Graham, Miss. Margaret Edith</td>
      <td>female</td>
      <td>19.0</td>
      <td>0</td>
      <td>0</td>
      <td>112053</td>
      <td>30.0000</td>
      <td>B42</td>
      <td>S</td>
    </tr>
    <tr>
      <th>888</th>
      <td>889</td>
      <td>0</td>
      <td>3</td>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
      <td>female</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>W./C. 6607</td>
      <td>23.4500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>889</th>
      <td>890</td>
      <td>1</td>
      <td>1</td>
      <td>Behr, Mr. Karl Howell</td>
      <td>male</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>111369</td>
      <td>30.0000</td>
      <td>C148</td>
      <td>C</td>
    </tr>
    <tr>
      <th>890</th>
      <td>891</td>
      <td>0</td>
      <td>3</td>
      <td>Dooley, Mr. Patrick</td>
      <td>male</td>
      <td>32.0</td>
      <td>0</td>
      <td>0</td>
      <td>370376</td>
      <td>7.7500</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 12 columns</p>
</div>




```python
df.head()
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
      <th>PassengerIndex</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.isnull()
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
      <th>PassengerIndex</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>886</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>887</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>888</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>889</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>890</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 12 columns</p>
</div>




```python
df['Cabin'].where(df['Cabin'].isnull())
```




    0      NaN
    1      NaN
    2      NaN
    3      NaN
    4      NaN
          ... 
    886    NaN
    887    NaN
    888    NaN
    889    NaN
    890    NaN
    Name: Cabin, Length: 891, dtype: object




```python
df.head()
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
      <th>PassengerIndex</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['Embarked'].count()

```




    <bound method Series.count of 0      S
    1      C
    2      S
    3      S
    4      S
          ..
    886    S
    887    S
    888    S
    889    C
    890    Q
    Name: Embarked, Length: 891, dtype: object>




```python
df['Cabin'].isnull().sum()
```




    687




```python
df['Cabin'].fillna('Harish', inplace=True)
```


```python
df['Cabin'].isnull().sum()
```




    0




```python
df.head()
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
      <th>PassengerIndex</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_values('Fare', ascending=False)
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
      <th>PassengerIndex</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>258</th>
      <td>259</td>
      <td>1</td>
      <td>1</td>
      <td>Ward, Miss. Anna</td>
      <td>female</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>PC 17755</td>
      <td>512.3292</td>
      <td>Harish</td>
      <td>C</td>
    </tr>
    <tr>
      <th>737</th>
      <td>738</td>
      <td>1</td>
      <td>1</td>
      <td>Lesurer, Mr. Gustave J</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>PC 17755</td>
      <td>512.3292</td>
      <td>B101</td>
      <td>C</td>
    </tr>
    <tr>
      <th>679</th>
      <td>680</td>
      <td>1</td>
      <td>1</td>
      <td>Cardeza, Mr. Thomas Drake Martinez</td>
      <td>male</td>
      <td>36.0</td>
      <td>0</td>
      <td>1</td>
      <td>PC 17755</td>
      <td>512.3292</td>
      <td>B51 B53 B55</td>
      <td>C</td>
    </tr>
    <tr>
      <th>88</th>
      <td>89</td>
      <td>1</td>
      <td>1</td>
      <td>Fortune, Miss. Mabel Helen</td>
      <td>female</td>
      <td>23.0</td>
      <td>3</td>
      <td>2</td>
      <td>19950</td>
      <td>263.0000</td>
      <td>C23 C25 C27</td>
      <td>S</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
      <td>0</td>
      <td>1</td>
      <td>Fortune, Mr. Charles Alexander</td>
      <td>male</td>
      <td>19.0</td>
      <td>3</td>
      <td>2</td>
      <td>19950</td>
      <td>263.0000</td>
      <td>C23 C25 C27</td>
      <td>S</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>633</th>
      <td>634</td>
      <td>0</td>
      <td>1</td>
      <td>Parr, Mr. William Henry Marsh</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>112052</td>
      <td>0.0000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>413</th>
      <td>414</td>
      <td>0</td>
      <td>2</td>
      <td>Cunningham, Mr. Alfred Fleming</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>239853</td>
      <td>0.0000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>822</th>
      <td>823</td>
      <td>0</td>
      <td>1</td>
      <td>Reuchlin, Jonkheer. John George</td>
      <td>male</td>
      <td>38.0</td>
      <td>0</td>
      <td>0</td>
      <td>19972</td>
      <td>0.0000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>732</th>
      <td>733</td>
      <td>0</td>
      <td>2</td>
      <td>Knight, Mr. Robert J</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>239855</td>
      <td>0.0000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>674</th>
      <td>675</td>
      <td>0</td>
      <td>2</td>
      <td>Watson, Mr. Ennis Hastings</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>239856</td>
      <td>0.0000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 12 columns</p>
</div>




```python
dfCopy = df.copy()
```


```python
dfCopy.sort_values('Fare', ascending=False)
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
      <th>PassengerIndex</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>258</th>
      <td>259</td>
      <td>1</td>
      <td>1</td>
      <td>Ward, Miss. Anna</td>
      <td>female</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>PC 17755</td>
      <td>512.3292</td>
      <td>Harish</td>
      <td>C</td>
    </tr>
    <tr>
      <th>737</th>
      <td>738</td>
      <td>1</td>
      <td>1</td>
      <td>Lesurer, Mr. Gustave J</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>PC 17755</td>
      <td>512.3292</td>
      <td>B101</td>
      <td>C</td>
    </tr>
    <tr>
      <th>679</th>
      <td>680</td>
      <td>1</td>
      <td>1</td>
      <td>Cardeza, Mr. Thomas Drake Martinez</td>
      <td>male</td>
      <td>36.0</td>
      <td>0</td>
      <td>1</td>
      <td>PC 17755</td>
      <td>512.3292</td>
      <td>B51 B53 B55</td>
      <td>C</td>
    </tr>
    <tr>
      <th>88</th>
      <td>89</td>
      <td>1</td>
      <td>1</td>
      <td>Fortune, Miss. Mabel Helen</td>
      <td>female</td>
      <td>23.0</td>
      <td>3</td>
      <td>2</td>
      <td>19950</td>
      <td>263.0000</td>
      <td>C23 C25 C27</td>
      <td>S</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
      <td>0</td>
      <td>1</td>
      <td>Fortune, Mr. Charles Alexander</td>
      <td>male</td>
      <td>19.0</td>
      <td>3</td>
      <td>2</td>
      <td>19950</td>
      <td>263.0000</td>
      <td>C23 C25 C27</td>
      <td>S</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>633</th>
      <td>634</td>
      <td>0</td>
      <td>1</td>
      <td>Parr, Mr. William Henry Marsh</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>112052</td>
      <td>0.0000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>413</th>
      <td>414</td>
      <td>0</td>
      <td>2</td>
      <td>Cunningham, Mr. Alfred Fleming</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>239853</td>
      <td>0.0000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>822</th>
      <td>823</td>
      <td>0</td>
      <td>1</td>
      <td>Reuchlin, Jonkheer. John George</td>
      <td>male</td>
      <td>38.0</td>
      <td>0</td>
      <td>0</td>
      <td>19972</td>
      <td>0.0000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>732</th>
      <td>733</td>
      <td>0</td>
      <td>2</td>
      <td>Knight, Mr. Robert J</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>239855</td>
      <td>0.0000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>674</th>
      <td>675</td>
      <td>0</td>
      <td>2</td>
      <td>Watson, Mr. Ennis Hastings</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>239856</td>
      <td>0.0000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 12 columns</p>
</div>




```python
df.drop(columns=['Parch'], axis=1, inplace=True)
```


```python
dfCopy.head()
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
      <th>PassengerIndex</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.head()
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
      <th>PassengerIndex</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[(df['Fare']>50) & (df['Pclass']==3)].sort_values('Fare', ascending=False)
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
      <th>PassengerIndex</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>159</th>
      <td>160</td>
      <td>0</td>
      <td>3</td>
      <td>Sage, Master. Thomas Henry</td>
      <td>male</td>
      <td>NaN</td>
      <td>8</td>
      <td>CA. 2343</td>
      <td>69.5500</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>180</th>
      <td>181</td>
      <td>0</td>
      <td>3</td>
      <td>Sage, Miss. Constance Gladys</td>
      <td>female</td>
      <td>NaN</td>
      <td>8</td>
      <td>CA. 2343</td>
      <td>69.5500</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>201</th>
      <td>202</td>
      <td>0</td>
      <td>3</td>
      <td>Sage, Mr. Frederick</td>
      <td>male</td>
      <td>NaN</td>
      <td>8</td>
      <td>CA. 2343</td>
      <td>69.5500</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>324</th>
      <td>325</td>
      <td>0</td>
      <td>3</td>
      <td>Sage, Mr. George John Jr</td>
      <td>male</td>
      <td>NaN</td>
      <td>8</td>
      <td>CA. 2343</td>
      <td>69.5500</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>792</th>
      <td>793</td>
      <td>0</td>
      <td>3</td>
      <td>Sage, Miss. Stella Anna</td>
      <td>female</td>
      <td>NaN</td>
      <td>8</td>
      <td>CA. 2343</td>
      <td>69.5500</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>846</th>
      <td>847</td>
      <td>0</td>
      <td>3</td>
      <td>Sage, Mr. Douglas Bullen</td>
      <td>male</td>
      <td>NaN</td>
      <td>8</td>
      <td>CA. 2343</td>
      <td>69.5500</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>863</th>
      <td>864</td>
      <td>0</td>
      <td>3</td>
      <td>Sage, Miss. Dorothy Edith "Dolly"</td>
      <td>female</td>
      <td>NaN</td>
      <td>8</td>
      <td>CA. 2343</td>
      <td>69.5500</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>74</th>
      <td>75</td>
      <td>1</td>
      <td>3</td>
      <td>Bing, Mr. Lee</td>
      <td>male</td>
      <td>32.0</td>
      <td>0</td>
      <td>1601</td>
      <td>56.4958</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>169</th>
      <td>170</td>
      <td>0</td>
      <td>3</td>
      <td>Ling, Mr. Lee</td>
      <td>male</td>
      <td>28.0</td>
      <td>0</td>
      <td>1601</td>
      <td>56.4958</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>509</th>
      <td>510</td>
      <td>1</td>
      <td>3</td>
      <td>Lang, Mr. Fang</td>
      <td>male</td>
      <td>26.0</td>
      <td>0</td>
      <td>1601</td>
      <td>56.4958</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>643</th>
      <td>644</td>
      <td>1</td>
      <td>3</td>
      <td>Foo, Mr. Choong</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>1601</td>
      <td>56.4958</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>692</th>
      <td>693</td>
      <td>1</td>
      <td>3</td>
      <td>Lam, Mr. Ali</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>1601</td>
      <td>56.4958</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>826</th>
      <td>827</td>
      <td>0</td>
      <td>3</td>
      <td>Lam, Mr. Len</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>1601</td>
      <td>56.4958</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>838</th>
      <td>839</td>
      <td>1</td>
      <td>3</td>
      <td>Chip, Mr. Chang</td>
      <td>male</td>
      <td>32.0</td>
      <td>0</td>
      <td>1601</td>
      <td>56.4958</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['Fare'].describe()
```




    count    891.000000
    mean      32.204208
    std       49.693429
    min        0.000000
    25%        7.910400
    50%       14.454200
    75%       31.000000
    max      512.329200
    Name: Fare, dtype: float64




```python
df['Fare'].mean()
```




    32.2042079685746




```python
df['Fare'].std()
```




    49.693428597180905




```python
df['Fare'].corr(df['Pclass'])
```




    -0.5494996199439072




```python
df[['Fare','Pclass']]
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
      <th>Fare</th>
      <th>Pclass</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7.2500</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>71.2833</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.9250</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>53.1000</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.0500</td>
      <td>3</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>886</th>
      <td>13.0000</td>
      <td>2</td>
    </tr>
    <tr>
      <th>887</th>
      <td>30.0000</td>
      <td>1</td>
    </tr>
    <tr>
      <th>888</th>
      <td>23.4500</td>
      <td>3</td>
    </tr>
    <tr>
      <th>889</th>
      <td>30.0000</td>
      <td>1</td>
    </tr>
    <tr>
      <th>890</th>
      <td>7.7500</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 2 columns</p>
</div>




```python
df[100:140]
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
      <th>PassengerIndex</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>100</th>
      <td>101</td>
      <td>0</td>
      <td>3</td>
      <td>Petranec, Miss. Matilda</td>
      <td>female</td>
      <td>28.0</td>
      <td>0</td>
      <td>349245</td>
      <td>7.8958</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>101</th>
      <td>102</td>
      <td>0</td>
      <td>3</td>
      <td>Petroff, Mr. Pastcho ("Pentcho")</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>349215</td>
      <td>7.8958</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>102</th>
      <td>103</td>
      <td>0</td>
      <td>1</td>
      <td>White, Mr. Richard Frasar</td>
      <td>male</td>
      <td>21.0</td>
      <td>0</td>
      <td>35281</td>
      <td>77.2875</td>
      <td>D26</td>
      <td>S</td>
    </tr>
    <tr>
      <th>103</th>
      <td>104</td>
      <td>0</td>
      <td>3</td>
      <td>Johansson, Mr. Gustaf Joel</td>
      <td>male</td>
      <td>33.0</td>
      <td>0</td>
      <td>7540</td>
      <td>8.6542</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>104</th>
      <td>105</td>
      <td>0</td>
      <td>3</td>
      <td>Gustafsson, Mr. Anders Vilhelm</td>
      <td>male</td>
      <td>37.0</td>
      <td>2</td>
      <td>3101276</td>
      <td>7.9250</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>105</th>
      <td>106</td>
      <td>0</td>
      <td>3</td>
      <td>Mionoff, Mr. Stoytcho</td>
      <td>male</td>
      <td>28.0</td>
      <td>0</td>
      <td>349207</td>
      <td>7.8958</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>106</th>
      <td>107</td>
      <td>1</td>
      <td>3</td>
      <td>Salkjelsvik, Miss. Anna Kristine</td>
      <td>female</td>
      <td>21.0</td>
      <td>0</td>
      <td>343120</td>
      <td>7.6500</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>107</th>
      <td>108</td>
      <td>1</td>
      <td>3</td>
      <td>Moss, Mr. Albert Johan</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>312991</td>
      <td>7.7750</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>108</th>
      <td>109</td>
      <td>0</td>
      <td>3</td>
      <td>Rekic, Mr. Tido</td>
      <td>male</td>
      <td>38.0</td>
      <td>0</td>
      <td>349249</td>
      <td>7.8958</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>109</th>
      <td>110</td>
      <td>1</td>
      <td>3</td>
      <td>Moran, Miss. Bertha</td>
      <td>female</td>
      <td>NaN</td>
      <td>1</td>
      <td>371110</td>
      <td>24.1500</td>
      <td>Harish</td>
      <td>Q</td>
    </tr>
    <tr>
      <th>110</th>
      <td>111</td>
      <td>0</td>
      <td>1</td>
      <td>Porter, Mr. Walter Chamberlain</td>
      <td>male</td>
      <td>47.0</td>
      <td>0</td>
      <td>110465</td>
      <td>52.0000</td>
      <td>C110</td>
      <td>S</td>
    </tr>
    <tr>
      <th>111</th>
      <td>112</td>
      <td>0</td>
      <td>3</td>
      <td>Zabour, Miss. Hileni</td>
      <td>female</td>
      <td>14.5</td>
      <td>1</td>
      <td>2665</td>
      <td>14.4542</td>
      <td>Harish</td>
      <td>C</td>
    </tr>
    <tr>
      <th>112</th>
      <td>113</td>
      <td>0</td>
      <td>3</td>
      <td>Barton, Mr. David John</td>
      <td>male</td>
      <td>22.0</td>
      <td>0</td>
      <td>324669</td>
      <td>8.0500</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>113</th>
      <td>114</td>
      <td>0</td>
      <td>3</td>
      <td>Jussila, Miss. Katriina</td>
      <td>female</td>
      <td>20.0</td>
      <td>1</td>
      <td>4136</td>
      <td>9.8250</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>114</th>
      <td>115</td>
      <td>0</td>
      <td>3</td>
      <td>Attalah, Miss. Malake</td>
      <td>female</td>
      <td>17.0</td>
      <td>0</td>
      <td>2627</td>
      <td>14.4583</td>
      <td>Harish</td>
      <td>C</td>
    </tr>
    <tr>
      <th>115</th>
      <td>116</td>
      <td>0</td>
      <td>3</td>
      <td>Pekoniemi, Mr. Edvard</td>
      <td>male</td>
      <td>21.0</td>
      <td>0</td>
      <td>STON/O 2. 3101294</td>
      <td>7.9250</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>116</th>
      <td>117</td>
      <td>0</td>
      <td>3</td>
      <td>Connors, Mr. Patrick</td>
      <td>male</td>
      <td>70.5</td>
      <td>0</td>
      <td>370369</td>
      <td>7.7500</td>
      <td>Harish</td>
      <td>Q</td>
    </tr>
    <tr>
      <th>117</th>
      <td>118</td>
      <td>0</td>
      <td>2</td>
      <td>Turpin, Mr. William John Robert</td>
      <td>male</td>
      <td>29.0</td>
      <td>1</td>
      <td>11668</td>
      <td>21.0000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>118</th>
      <td>119</td>
      <td>0</td>
      <td>1</td>
      <td>Baxter, Mr. Quigg Edmond</td>
      <td>male</td>
      <td>24.0</td>
      <td>0</td>
      <td>PC 17558</td>
      <td>247.5208</td>
      <td>B58 B60</td>
      <td>C</td>
    </tr>
    <tr>
      <th>119</th>
      <td>120</td>
      <td>0</td>
      <td>3</td>
      <td>Andersson, Miss. Ellis Anna Maria</td>
      <td>female</td>
      <td>2.0</td>
      <td>4</td>
      <td>347082</td>
      <td>31.2750</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>120</th>
      <td>121</td>
      <td>0</td>
      <td>2</td>
      <td>Hickman, Mr. Stanley George</td>
      <td>male</td>
      <td>21.0</td>
      <td>2</td>
      <td>S.O.C. 14879</td>
      <td>73.5000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>121</th>
      <td>122</td>
      <td>0</td>
      <td>3</td>
      <td>Moore, Mr. Leonard Charles</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>A4. 54510</td>
      <td>8.0500</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>122</th>
      <td>123</td>
      <td>0</td>
      <td>2</td>
      <td>Nasser, Mr. Nicholas</td>
      <td>male</td>
      <td>32.5</td>
      <td>1</td>
      <td>237736</td>
      <td>30.0708</td>
      <td>Harish</td>
      <td>C</td>
    </tr>
    <tr>
      <th>123</th>
      <td>124</td>
      <td>1</td>
      <td>2</td>
      <td>Webber, Miss. Susan</td>
      <td>female</td>
      <td>32.5</td>
      <td>0</td>
      <td>27267</td>
      <td>13.0000</td>
      <td>E101</td>
      <td>S</td>
    </tr>
    <tr>
      <th>124</th>
      <td>125</td>
      <td>0</td>
      <td>1</td>
      <td>White, Mr. Percival Wayland</td>
      <td>male</td>
      <td>54.0</td>
      <td>0</td>
      <td>35281</td>
      <td>77.2875</td>
      <td>D26</td>
      <td>S</td>
    </tr>
    <tr>
      <th>125</th>
      <td>126</td>
      <td>1</td>
      <td>3</td>
      <td>Nicola-Yarred, Master. Elias</td>
      <td>male</td>
      <td>12.0</td>
      <td>1</td>
      <td>2651</td>
      <td>11.2417</td>
      <td>Harish</td>
      <td>C</td>
    </tr>
    <tr>
      <th>126</th>
      <td>127</td>
      <td>0</td>
      <td>3</td>
      <td>McMahon, Mr. Martin</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>370372</td>
      <td>7.7500</td>
      <td>Harish</td>
      <td>Q</td>
    </tr>
    <tr>
      <th>127</th>
      <td>128</td>
      <td>1</td>
      <td>3</td>
      <td>Madsen, Mr. Fridtjof Arne</td>
      <td>male</td>
      <td>24.0</td>
      <td>0</td>
      <td>C 17369</td>
      <td>7.1417</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>128</th>
      <td>129</td>
      <td>1</td>
      <td>3</td>
      <td>Peter, Miss. Anna</td>
      <td>female</td>
      <td>NaN</td>
      <td>1</td>
      <td>2668</td>
      <td>22.3583</td>
      <td>F E69</td>
      <td>C</td>
    </tr>
    <tr>
      <th>129</th>
      <td>130</td>
      <td>0</td>
      <td>3</td>
      <td>Ekstrom, Mr. Johan</td>
      <td>male</td>
      <td>45.0</td>
      <td>0</td>
      <td>347061</td>
      <td>6.9750</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>130</th>
      <td>131</td>
      <td>0</td>
      <td>3</td>
      <td>Drazenoic, Mr. Jozef</td>
      <td>male</td>
      <td>33.0</td>
      <td>0</td>
      <td>349241</td>
      <td>7.8958</td>
      <td>Harish</td>
      <td>C</td>
    </tr>
    <tr>
      <th>131</th>
      <td>132</td>
      <td>0</td>
      <td>3</td>
      <td>Coelho, Mr. Domingos Fernandeo</td>
      <td>male</td>
      <td>20.0</td>
      <td>0</td>
      <td>SOTON/O.Q. 3101307</td>
      <td>7.0500</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>132</th>
      <td>133</td>
      <td>0</td>
      <td>3</td>
      <td>Robins, Mrs. Alexander A (Grace Charity Laury)</td>
      <td>female</td>
      <td>47.0</td>
      <td>1</td>
      <td>A/5. 3337</td>
      <td>14.5000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>133</th>
      <td>134</td>
      <td>1</td>
      <td>2</td>
      <td>Weisz, Mrs. Leopold (Mathilde Francoise Pede)</td>
      <td>female</td>
      <td>29.0</td>
      <td>1</td>
      <td>228414</td>
      <td>26.0000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>134</th>
      <td>135</td>
      <td>0</td>
      <td>2</td>
      <td>Sobey, Mr. Samuel James Hayden</td>
      <td>male</td>
      <td>25.0</td>
      <td>0</td>
      <td>C.A. 29178</td>
      <td>13.0000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>135</th>
      <td>136</td>
      <td>0</td>
      <td>2</td>
      <td>Richard, Mr. Emile</td>
      <td>male</td>
      <td>23.0</td>
      <td>0</td>
      <td>SC/PARIS 2133</td>
      <td>15.0458</td>
      <td>Harish</td>
      <td>C</td>
    </tr>
    <tr>
      <th>136</th>
      <td>137</td>
      <td>1</td>
      <td>1</td>
      <td>Newsom, Miss. Helen Monypeny</td>
      <td>female</td>
      <td>19.0</td>
      <td>0</td>
      <td>11752</td>
      <td>26.2833</td>
      <td>D47</td>
      <td>S</td>
    </tr>
    <tr>
      <th>137</th>
      <td>138</td>
      <td>0</td>
      <td>1</td>
      <td>Futrelle, Mr. Jacques Heath</td>
      <td>male</td>
      <td>37.0</td>
      <td>1</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>138</th>
      <td>139</td>
      <td>0</td>
      <td>3</td>
      <td>Osen, Mr. Olaf Elon</td>
      <td>male</td>
      <td>16.0</td>
      <td>0</td>
      <td>7534</td>
      <td>9.2167</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>139</th>
      <td>140</td>
      <td>0</td>
      <td>1</td>
      <td>Giglio, Mr. Victor</td>
      <td>male</td>
      <td>24.0</td>
      <td>0</td>
      <td>PC 17593</td>
      <td>79.2000</td>
      <td>B86</td>
      <td>C</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[100]
```




    PassengerIndex                        101
    Survived                                0
    Pclass                                  3
    Name              Petranec, Miss. Matilda
    Sex                                female
    Age                                  28.0
    SibSp                                   0
    Ticket                             349245
    Fare                               7.8958
    Cabin                              Harish
    Embarked                                S
    Name: 100, dtype: object




```python
df.sort_values('Fare', ascending=False)
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
      <th>PassengerIndex</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>258</th>
      <td>259</td>
      <td>1</td>
      <td>1</td>
      <td>Ward, Miss. Anna</td>
      <td>female</td>
      <td>35.0</td>
      <td>0</td>
      <td>PC 17755</td>
      <td>512.3292</td>
      <td>Harish</td>
      <td>C</td>
    </tr>
    <tr>
      <th>737</th>
      <td>738</td>
      <td>1</td>
      <td>1</td>
      <td>Lesurer, Mr. Gustave J</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>PC 17755</td>
      <td>512.3292</td>
      <td>B101</td>
      <td>C</td>
    </tr>
    <tr>
      <th>679</th>
      <td>680</td>
      <td>1</td>
      <td>1</td>
      <td>Cardeza, Mr. Thomas Drake Martinez</td>
      <td>male</td>
      <td>36.0</td>
      <td>0</td>
      <td>PC 17755</td>
      <td>512.3292</td>
      <td>B51 B53 B55</td>
      <td>C</td>
    </tr>
    <tr>
      <th>88</th>
      <td>89</td>
      <td>1</td>
      <td>1</td>
      <td>Fortune, Miss. Mabel Helen</td>
      <td>female</td>
      <td>23.0</td>
      <td>3</td>
      <td>19950</td>
      <td>263.0000</td>
      <td>C23 C25 C27</td>
      <td>S</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
      <td>0</td>
      <td>1</td>
      <td>Fortune, Mr. Charles Alexander</td>
      <td>male</td>
      <td>19.0</td>
      <td>3</td>
      <td>19950</td>
      <td>263.0000</td>
      <td>C23 C25 C27</td>
      <td>S</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>633</th>
      <td>634</td>
      <td>0</td>
      <td>1</td>
      <td>Parr, Mr. William Henry Marsh</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>112052</td>
      <td>0.0000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>413</th>
      <td>414</td>
      <td>0</td>
      <td>2</td>
      <td>Cunningham, Mr. Alfred Fleming</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>239853</td>
      <td>0.0000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>822</th>
      <td>823</td>
      <td>0</td>
      <td>1</td>
      <td>Reuchlin, Jonkheer. John George</td>
      <td>male</td>
      <td>38.0</td>
      <td>0</td>
      <td>19972</td>
      <td>0.0000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>732</th>
      <td>733</td>
      <td>0</td>
      <td>2</td>
      <td>Knight, Mr. Robert J</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>239855</td>
      <td>0.0000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
    <tr>
      <th>674</th>
      <td>675</td>
      <td>0</td>
      <td>2</td>
      <td>Watson, Mr. Ennis Hastings</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>239856</td>
      <td>0.0000</td>
      <td>Harish</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 11 columns</p>
</div>




```python
df['newCol'] = df['Fare'].map(str) + '_' + df['Pclass'].map(str)
```


```python
df.head()
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
      <th>PassengerIndex</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>newCol</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>Harish</td>
      <td>S</td>
      <td>7.25_3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>71.2833_1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>Harish</td>
      <td>S</td>
      <td>7.925_3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
      <td>53.1_1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>Harish</td>
      <td>S</td>
      <td>8.05_3</td>
    </tr>
  </tbody>
</table>
</div>




```python
import pandas as pd
df = pd.DataFrame({'Courses': ["Spark","PySpark","Python","pandas","Java"],
                    'Fee' : [20000,25000,30000,24000,40000],
                    'Duration':['30day','40days','60days','55days','50days']})

df1 = pd.DataFrame({'Courses': ["Java","PySpark","Python","pandas","Hyperion"],
                    'Fee': [20000,25000,30000,24000,40000],
                    'Percentage':['10%','20%','25%','20%','10%']})
 
print(df)
print(df1)

# Merge default pandas DataFrame without any key column
merged_df = pd.merge(df,df1)
print(merged_df)

# Use pandas.merge() to on multiple columns
df2 = pd.merge(df, df1,  how='left', left_on=['Courses','Fee'], right_on = ['Courses','Fee'])
print(df2)

# Merge Pandas DataFrames using left_on and right_on
merged_df = pd.merge(df, df1, left_on="Courses", right_on="Courses")
print(merged_df)

# Set value of on parameter to specify the key value for merge in pandas
merged_df = pd.merge(df, df1, on="Courses")
print(merged_df)
```

       Courses    Fee Duration
    0    Spark  20000    30day
    1  PySpark  25000   40days
    2   Python  30000   60days
    3   pandas  24000   55days
    4     Java  40000   50days
        Courses    Fee Percentage
    0      Java  20000        10%
    1   PySpark  25000        20%
    2    Python  30000        25%
    3    pandas  24000        20%
    4  Hyperion  40000        10%
       Courses    Fee Duration Percentage
    0  PySpark  25000   40days        20%
    1   Python  30000   60days        25%
    2   pandas  24000   55days        20%
       Courses    Fee Duration Percentage
    0    Spark  20000    30day        NaN
    1  PySpark  25000   40days        20%
    2   Python  30000   60days        25%
    3   pandas  24000   55days        20%
    4     Java  40000   50days        NaN
       Courses  Fee_x Duration  Fee_y Percentage
    0  PySpark  25000   40days  25000        20%
    1   Python  30000   60days  30000        25%
    2   pandas  24000   55days  24000        20%
    3     Java  40000   50days  20000        10%
       Courses  Fee_x Duration  Fee_y Percentage
    0  PySpark  25000   40days  25000        20%
    1   Python  30000   60days  30000        25%
    2   pandas  24000   55days  24000        20%
    3     Java  40000   50days  20000        10%
    


```python
df.head()
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
      <th>Courses</th>
      <th>Fee</th>
      <th>Duration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Spark</td>
      <td>20000</td>
      <td>30day</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PySpark</td>
      <td>25000</td>
      <td>40days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Python</td>
      <td>30000</td>
      <td>60days</td>
    </tr>
    <tr>
      <th>3</th>
      <td>pandas</td>
      <td>24000</td>
      <td>55days</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Java</td>
      <td>40000</td>
      <td>50days</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['Fee'].dtype
```




    dtype('int64')




```python
df['Fee']=df['Fee'].astype('float')
```


```python
df['Fee'].dtype
```




    dtype('float64')




```python

```
