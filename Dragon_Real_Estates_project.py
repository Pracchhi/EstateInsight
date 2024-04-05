{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "72ebde3e",
   "metadata": {},
   "source": [
    "#   Dragon Real Estate - Price Predictor\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "30c032f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a8dee9be",
   "metadata": {},
   "outputs": [],
   "source": [
    "housing = pd.read_csv(\"data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7ff3be0c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CRIM</th>\n",
       "      <th>ZN</th>\n",
       "      <th>INDUS</th>\n",
       "      <th>CHAS</th>\n",
       "      <th>NOX</th>\n",
       "      <th>RM</th>\n",
       "      <th>AGE</th>\n",
       "      <th>DIS</th>\n",
       "      <th>RAD</th>\n",
       "      <th>TAX</th>\n",
       "      <th>PTRATIO</th>\n",
       "      <th>B</th>\n",
       "      <th>LSTAT</th>\n",
       "      <th>MEDV</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.00632</td>\n",
       "      <td>18.0</td>\n",
       "      <td>2.31</td>\n",
       "      <td>0</td>\n",
       "      <td>0.538</td>\n",
       "      <td>6.575</td>\n",
       "      <td>65.2</td>\n",
       "      <td>4.0900</td>\n",
       "      <td>1</td>\n",
       "      <td>296</td>\n",
       "      <td>15.3</td>\n",
       "      <td>396.90</td>\n",
       "      <td>4.98</td>\n",
       "      <td>24.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.02731</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.07</td>\n",
       "      <td>0</td>\n",
       "      <td>0.469</td>\n",
       "      <td>6.421</td>\n",
       "      <td>78.9</td>\n",
       "      <td>4.9671</td>\n",
       "      <td>2</td>\n",
       "      <td>242</td>\n",
       "      <td>17.8</td>\n",
       "      <td>396.90</td>\n",
       "      <td>9.14</td>\n",
       "      <td>21.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.02729</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.07</td>\n",
       "      <td>0</td>\n",
       "      <td>0.469</td>\n",
       "      <td>7.185</td>\n",
       "      <td>61.1</td>\n",
       "      <td>4.9671</td>\n",
       "      <td>2</td>\n",
       "      <td>242</td>\n",
       "      <td>17.8</td>\n",
       "      <td>392.83</td>\n",
       "      <td>4.03</td>\n",
       "      <td>34.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.03237</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2.18</td>\n",
       "      <td>0</td>\n",
       "      <td>0.458</td>\n",
       "      <td>6.998</td>\n",
       "      <td>45.8</td>\n",
       "      <td>6.0622</td>\n",
       "      <td>3</td>\n",
       "      <td>222</td>\n",
       "      <td>18.7</td>\n",
       "      <td>394.63</td>\n",
       "      <td>2.94</td>\n",
       "      <td>33.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.06905</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2.18</td>\n",
       "      <td>0</td>\n",
       "      <td>0.458</td>\n",
       "      <td>7.147</td>\n",
       "      <td>54.2</td>\n",
       "      <td>6.0622</td>\n",
       "      <td>3</td>\n",
       "      <td>222</td>\n",
       "      <td>18.7</td>\n",
       "      <td>396.90</td>\n",
       "      <td>5.33</td>\n",
       "      <td>36.2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      CRIM    ZN  INDUS  CHAS    NOX     RM   AGE     DIS  RAD  TAX  PTRATIO  \\\n",
       "0  0.00632  18.0   2.31     0  0.538  6.575  65.2  4.0900    1  296     15.3   \n",
       "1  0.02731   0.0   7.07     0  0.469  6.421  78.9  4.9671    2  242     17.8   \n",
       "2  0.02729   0.0   7.07     0  0.469  7.185  61.1  4.9671    2  242     17.8   \n",
       "3  0.03237   0.0   2.18     0  0.458  6.998  45.8  6.0622    3  222     18.7   \n",
       "4  0.06905   0.0   2.18     0  0.458  7.147  54.2  6.0622    3  222     18.7   \n",
       "\n",
       "        B  LSTAT  MEDV  \n",
       "0  396.90   4.98  24.0  \n",
       "1  396.90   9.14  21.6  \n",
       "2  392.83   4.03  34.7  \n",
       "3  394.63   2.94  33.4  \n",
       "4  396.90   5.33  36.2  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "housing.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0f520ba3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 506 entries, 0 to 505\n",
      "Data columns (total 14 columns):\n",
      " #   Column   Non-Null Count  Dtype  \n",
      "---  ------   --------------  -----  \n",
      " 0   CRIM     506 non-null    float64\n",
      " 1   ZN       506 non-null    float64\n",
      " 2   INDUS    506 non-null    float64\n",
      " 3   CHAS     506 non-null    int64  \n",
      " 4   NOX      506 non-null    float64\n",
      " 5   RM       506 non-null    float64\n",
      " 6   AGE      506 non-null    float64\n",
      " 7   DIS      506 non-null    float64\n",
      " 8   RAD      506 non-null    int64  \n",
      " 9   TAX      506 non-null    int64  \n",
      " 10  PTRATIO  506 non-null    float64\n",
      " 11  B        506 non-null    float64\n",
      " 12  LSTAT    506 non-null    float64\n",
      " 13  MEDV     506 non-null    float64\n",
      "dtypes: float64(11), int64(3)\n",
      "memory usage: 55.5 KB\n"
     ]
    }
   ],
   "source": [
    "housing.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5adb0508",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    471\n",
       "1     35\n",
       "Name: CHAS, dtype: int64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "housing['CHAS'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d5cfcd9e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CRIM</th>\n",
       "      <th>ZN</th>\n",
       "      <th>INDUS</th>\n",
       "      <th>CHAS</th>\n",
       "      <th>NOX</th>\n",
       "      <th>RM</th>\n",
       "      <th>AGE</th>\n",
       "      <th>DIS</th>\n",
       "      <th>RAD</th>\n",
       "      <th>TAX</th>\n",
       "      <th>PTRATIO</th>\n",
       "      <th>B</th>\n",
       "      <th>LSTAT</th>\n",
       "      <th>MEDV</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>3.613524</td>\n",
       "      <td>11.363636</td>\n",
       "      <td>11.136779</td>\n",
       "      <td>0.069170</td>\n",
       "      <td>0.554695</td>\n",
       "      <td>6.284634</td>\n",
       "      <td>68.574901</td>\n",
       "      <td>3.795043</td>\n",
       "      <td>9.549407</td>\n",
       "      <td>408.237154</td>\n",
       "      <td>18.455534</td>\n",
       "      <td>356.674032</td>\n",
       "      <td>12.653063</td>\n",
       "      <td>22.532806</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>8.601545</td>\n",
       "      <td>23.322453</td>\n",
       "      <td>6.860353</td>\n",
       "      <td>0.253994</td>\n",
       "      <td>0.115878</td>\n",
       "      <td>0.702617</td>\n",
       "      <td>28.148861</td>\n",
       "      <td>2.105710</td>\n",
       "      <td>8.707259</td>\n",
       "      <td>168.537116</td>\n",
       "      <td>2.164946</td>\n",
       "      <td>91.294864</td>\n",
       "      <td>7.141062</td>\n",
       "      <td>9.197104</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.006320</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.460000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.385000</td>\n",
       "      <td>3.561000</td>\n",
       "      <td>2.900000</td>\n",
       "      <td>1.129600</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>187.000000</td>\n",
       "      <td>12.600000</td>\n",
       "      <td>0.320000</td>\n",
       "      <td>1.730000</td>\n",
       "      <td>5.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.082045</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>5.190000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.449000</td>\n",
       "      <td>5.885500</td>\n",
       "      <td>45.025000</td>\n",
       "      <td>2.100175</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>279.000000</td>\n",
       "      <td>17.400000</td>\n",
       "      <td>375.377500</td>\n",
       "      <td>6.950000</td>\n",
       "      <td>17.025000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>0.256510</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>9.690000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.538000</td>\n",
       "      <td>6.208500</td>\n",
       "      <td>77.500000</td>\n",
       "      <td>3.207450</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>330.000000</td>\n",
       "      <td>19.050000</td>\n",
       "      <td>391.440000</td>\n",
       "      <td>11.360000</td>\n",
       "      <td>21.200000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>3.677083</td>\n",
       "      <td>12.500000</td>\n",
       "      <td>18.100000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.624000</td>\n",
       "      <td>6.623500</td>\n",
       "      <td>94.075000</td>\n",
       "      <td>5.188425</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>666.000000</td>\n",
       "      <td>20.200000</td>\n",
       "      <td>396.225000</td>\n",
       "      <td>16.955000</td>\n",
       "      <td>25.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>88.976200</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>27.740000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.871000</td>\n",
       "      <td>8.780000</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>12.126500</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>711.000000</td>\n",
       "      <td>22.000000</td>\n",
       "      <td>396.900000</td>\n",
       "      <td>37.970000</td>\n",
       "      <td>50.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             CRIM          ZN       INDUS        CHAS         NOX          RM  \\\n",
       "count  506.000000  506.000000  506.000000  506.000000  506.000000  506.000000   \n",
       "mean     3.613524   11.363636   11.136779    0.069170    0.554695    6.284634   \n",
       "std      8.601545   23.322453    6.860353    0.253994    0.115878    0.702617   \n",
       "min      0.006320    0.000000    0.460000    0.000000    0.385000    3.561000   \n",
       "25%      0.082045    0.000000    5.190000    0.000000    0.449000    5.885500   \n",
       "50%      0.256510    0.000000    9.690000    0.000000    0.538000    6.208500   \n",
       "75%      3.677083   12.500000   18.100000    0.000000    0.624000    6.623500   \n",
       "max     88.976200  100.000000   27.740000    1.000000    0.871000    8.780000   \n",
       "\n",
       "              AGE         DIS         RAD         TAX     PTRATIO           B  \\\n",
       "count  506.000000  506.000000  506.000000  506.000000  506.000000  506.000000   \n",
       "mean    68.574901    3.795043    9.549407  408.237154   18.455534  356.674032   \n",
       "std     28.148861    2.105710    8.707259  168.537116    2.164946   91.294864   \n",
       "min      2.900000    1.129600    1.000000  187.000000   12.600000    0.320000   \n",
       "25%     45.025000    2.100175    4.000000  279.000000   17.400000  375.377500   \n",
       "50%     77.500000    3.207450    5.000000  330.000000   19.050000  391.440000   \n",
       "75%     94.075000    5.188425   24.000000  666.000000   20.200000  396.225000   \n",
       "max    100.000000   12.126500   24.000000  711.000000   22.000000  396.900000   \n",
       "\n",
       "            LSTAT        MEDV  \n",
       "count  506.000000  506.000000  \n",
       "mean    12.653063   22.532806  \n",
       "std      7.141062    9.197104  \n",
       "min      1.730000    5.000000  \n",
       "25%      6.950000   17.025000  \n",
       "50%     11.360000   21.200000  \n",
       "75%     16.955000   25.000000  \n",
       "max     37.970000   50.000000  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "housing.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ab00114f",
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "89091dff",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b1fc8caa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[<AxesSubplot:title={'center':'CRIM'}>,\n",
       "        <AxesSubplot:title={'center':'ZN'}>,\n",
       "        <AxesSubplot:title={'center':'INDUS'}>,\n",
       "        <AxesSubplot:title={'center':'CHAS'}>],\n",
       "       [<AxesSubplot:title={'center':'NOX'}>,\n",
       "        <AxesSubplot:title={'center':'RM'}>,\n",
       "        <AxesSubplot:title={'center':'AGE'}>,\n",
       "        <AxesSubplot:title={'center':'DIS'}>],\n",
       "       [<AxesSubplot:title={'center':'RAD'}>,\n",
       "        <AxesSubplot:title={'center':'TAX'}>,\n",
       "        <AxesSubplot:title={'center':'PTRATIO'}>,\n",
       "        <AxesSubplot:title={'center':'B'}>],\n",
       "       [<AxesSubplot:title={'center':'LSTAT'}>,\n",
       "        <AxesSubplot:title={'center':'MEDV'}>, <AxesSubplot:>,\n",
       "        <AxesSubplot:>]], dtype=object)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x1080 with 16 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "housing.hist(bins=50, figsize=(20,15))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "01f05aa8",
   "metadata": {},
   "source": [
    "## Train-Test Splitting "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "aad19c87",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "def split_train_test(data,test_ratio):\n",
    "    np.random.seed(42)\n",
    "    shuffled = np.random.permutation(len(data))\n",
    "    print(shuffled)\n",
    "    test_set_size = int(len(data) * test_ratio)\n",
    "    test_indices = shuffled[:test_set_size]\n",
    "    train_indices = shuffled[test_set_size:]\n",
    "    return data.iloc[train_indices], data.iloc[test_indices]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "6ec13dac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[173 274 491  72 452  76 316 140 471 500 218   9 414  78 323 473 124 388\n",
      " 195 448 271 278  30 501 421 474  79 454 210 497 172 320 375 362 467 153\n",
      "   2 336 208  73 496 307 204  68  90 390  33  70 470   0  11 281  22 101\n",
      " 268 485 442 290  84 245  63  55 229  18 351 209 395  82  39 456  46 481\n",
      " 444 355  77 398 104 203 381 489  69 408 255 392 312 234 460 324  93 137\n",
      " 176 417 131 346 365 132 371 412 436 411  86  75 477  15 332 423  19 325\n",
      " 335  56 437 409 334 181 227 434 180  25 493 238 244 250 418 117  42 322\n",
      " 347 182 155 280 126 329  31 113 148 432 338  57 194  24  17 298  66 211\n",
      " 404  94 154 441  23 225 433 447   5 116  45  16 468 360   3 405 185  60\n",
      " 110 321 265  29 262 478  26   7 492 108  37 157 472 118 114 175 192 272\n",
      " 144 373 383 356 277 220 450 141 369  67 361 168 499 394 400 193 249 109\n",
      " 420 145  92 152 222 304  83 248 165 163 199 231  74 311 455 253 119 284\n",
      " 302 483 357 403 228 261 237 386 476  36 196 139 368 247 287 378  59 111\n",
      "  89 266   6 364 503 341 158 150 177 397 184 318  10 384 103  81  38 317\n",
      " 167 475 299 296 198 377 146 396 147 428 289 123 490  96 143 239 275  97\n",
      " 353 122 183 202 246 484 301 354 410 399 286 125 305 223 422 219 129 424\n",
      " 291 331 380 480 358 297 294 370 438 112 179 310 342 333 487 457 233 314\n",
      " 164 136 197 258 232 115 120 352 224 406 340 127 285 415 107 374 449 133\n",
      " 367  44 495  65 283  85 242 186 425 159  12  35  28 170 142 402 349 221\n",
      "  95  51 240 376 382 178  41 440 391 206 282 254 416   4 256 453 100 226\n",
      " 431 213 426 171  98 292 215  61  47  32 267 327 200 451  27 393 230 260\n",
      " 288 162 429 138  62 135 128 482   8 326 469  64 300  14 156  40 379 465\n",
      " 407 216 279 439 504 337 236 207 212 295 462 251 494 464 303 350 269 201\n",
      " 161  43 217 401 190 309 259 105  53 389   1 446 488  49 419  80 205  34\n",
      " 430 263 427 366  91 339 479  52 345 264 241  13 315  88 387 273 166 328\n",
      " 498 134 306 486 319 243  54 363  50 461 174 445 189 502 463 187 169  58\n",
      "  48 344 235 252  21 313 459 160 276 443 191 385 293 413 343 257 308 149\n",
      " 130 151 359  99 372  87 458 330 214 466 121 505  20 188  71 106 270 348\n",
      " 435 102]\n"
     ]
    }
   ],
   "source": [
    "train_set, test_set = split_train_test(housing, 0.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "844dc875",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rows in train set: 405\n",
      "Rows in test set: 101\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(f\"Rows in train set: {len(train_set)}\\nRows in test set: {len(test_set)}\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "395bce18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rows in train set: 404\n",
      "Rows in test set: 102\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "train_set, test_set = train_test_split(housing,test_size=0.2,random_state=42)\n",
    "print(f\"Rows in train set: {len(train_set)}\\nRows in test set: {len(test_set)}\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "4bc1c352",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import StratifiedShuffleSplit\n",
    "split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)\n",
    "for train_index, test_index in split.split(housing, housing['CHAS']):\n",
    "    strat_train_set = housing.loc[train_index]\n",
    "    strat_test_set = housing.loc[test_index]\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "482803a8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CRIM</th>\n",
       "      <th>ZN</th>\n",
       "      <th>INDUS</th>\n",
       "      <th>CHAS</th>\n",
       "      <th>NOX</th>\n",
       "      <th>RM</th>\n",
       "      <th>AGE</th>\n",
       "      <th>DIS</th>\n",
       "      <th>RAD</th>\n",
       "      <th>TAX</th>\n",
       "      <th>PTRATIO</th>\n",
       "      <th>B</th>\n",
       "      <th>LSTAT</th>\n",
       "      <th>MEDV</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>342</th>\n",
       "      <td>0.02498</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.89</td>\n",
       "      <td>0</td>\n",
       "      <td>0.518</td>\n",
       "      <td>6.540</td>\n",
       "      <td>59.7</td>\n",
       "      <td>6.2669</td>\n",
       "      <td>1</td>\n",
       "      <td>422</td>\n",
       "      <td>15.9</td>\n",
       "      <td>389.96</td>\n",
       "      <td>8.65</td>\n",
       "      <td>16.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>379</th>\n",
       "      <td>17.86670</td>\n",
       "      <td>0.0</td>\n",
       "      <td>18.10</td>\n",
       "      <td>0</td>\n",
       "      <td>0.671</td>\n",
       "      <td>6.223</td>\n",
       "      <td>100.0</td>\n",
       "      <td>1.3861</td>\n",
       "      <td>24</td>\n",
       "      <td>666</td>\n",
       "      <td>20.2</td>\n",
       "      <td>393.74</td>\n",
       "      <td>21.78</td>\n",
       "      <td>10.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>223</th>\n",
       "      <td>0.61470</td>\n",
       "      <td>0.0</td>\n",
       "      <td>6.20</td>\n",
       "      <td>0</td>\n",
       "      <td>0.507</td>\n",
       "      <td>6.618</td>\n",
       "      <td>80.8</td>\n",
       "      <td>3.2721</td>\n",
       "      <td>8</td>\n",
       "      <td>307</td>\n",
       "      <td>17.4</td>\n",
       "      <td>396.90</td>\n",
       "      <td>7.60</td>\n",
       "      <td>30.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>219</th>\n",
       "      <td>0.11425</td>\n",
       "      <td>0.0</td>\n",
       "      <td>13.89</td>\n",
       "      <td>1</td>\n",
       "      <td>0.550</td>\n",
       "      <td>6.373</td>\n",
       "      <td>92.4</td>\n",
       "      <td>3.3633</td>\n",
       "      <td>5</td>\n",
       "      <td>276</td>\n",
       "      <td>16.4</td>\n",
       "      <td>393.74</td>\n",
       "      <td>10.50</td>\n",
       "      <td>23.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>48</th>\n",
       "      <td>0.25387</td>\n",
       "      <td>0.0</td>\n",
       "      <td>6.91</td>\n",
       "      <td>0</td>\n",
       "      <td>0.448</td>\n",
       "      <td>5.399</td>\n",
       "      <td>95.3</td>\n",
       "      <td>5.8700</td>\n",
       "      <td>3</td>\n",
       "      <td>233</td>\n",
       "      <td>17.9</td>\n",
       "      <td>396.90</td>\n",
       "      <td>30.81</td>\n",
       "      <td>14.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>88</th>\n",
       "      <td>0.05660</td>\n",
       "      <td>0.0</td>\n",
       "      <td>3.41</td>\n",
       "      <td>0</td>\n",
       "      <td>0.489</td>\n",
       "      <td>7.007</td>\n",
       "      <td>86.3</td>\n",
       "      <td>3.4217</td>\n",
       "      <td>2</td>\n",
       "      <td>270</td>\n",
       "      <td>17.8</td>\n",
       "      <td>396.90</td>\n",
       "      <td>5.50</td>\n",
       "      <td>23.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>466</th>\n",
       "      <td>3.77498</td>\n",
       "      <td>0.0</td>\n",
       "      <td>18.10</td>\n",
       "      <td>0</td>\n",
       "      <td>0.655</td>\n",
       "      <td>5.952</td>\n",
       "      <td>84.7</td>\n",
       "      <td>2.8715</td>\n",
       "      <td>24</td>\n",
       "      <td>666</td>\n",
       "      <td>20.2</td>\n",
       "      <td>22.01</td>\n",
       "      <td>17.15</td>\n",
       "      <td>19.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>52</th>\n",
       "      <td>0.05360</td>\n",
       "      <td>21.0</td>\n",
       "      <td>5.64</td>\n",
       "      <td>0</td>\n",
       "      <td>0.439</td>\n",
       "      <td>6.511</td>\n",
       "      <td>21.1</td>\n",
       "      <td>6.8147</td>\n",
       "      <td>4</td>\n",
       "      <td>243</td>\n",
       "      <td>16.8</td>\n",
       "      <td>396.90</td>\n",
       "      <td>5.28</td>\n",
       "      <td>25.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>121</th>\n",
       "      <td>0.07165</td>\n",
       "      <td>0.0</td>\n",
       "      <td>25.65</td>\n",
       "      <td>0</td>\n",
       "      <td>0.581</td>\n",
       "      <td>6.004</td>\n",
       "      <td>84.1</td>\n",
       "      <td>2.1974</td>\n",
       "      <td>2</td>\n",
       "      <td>188</td>\n",
       "      <td>19.1</td>\n",
       "      <td>377.67</td>\n",
       "      <td>14.27</td>\n",
       "      <td>20.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>218</th>\n",
       "      <td>0.11069</td>\n",
       "      <td>0.0</td>\n",
       "      <td>13.89</td>\n",
       "      <td>1</td>\n",
       "      <td>0.550</td>\n",
       "      <td>5.951</td>\n",
       "      <td>93.8</td>\n",
       "      <td>2.8893</td>\n",
       "      <td>5</td>\n",
       "      <td>276</td>\n",
       "      <td>16.4</td>\n",
       "      <td>396.90</td>\n",
       "      <td>17.92</td>\n",
       "      <td>21.5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>102 rows × 14 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         CRIM    ZN  INDUS  CHAS    NOX     RM    AGE     DIS  RAD  TAX  \\\n",
       "342   0.02498   0.0   1.89     0  0.518  6.540   59.7  6.2669    1  422   \n",
       "379  17.86670   0.0  18.10     0  0.671  6.223  100.0  1.3861   24  666   \n",
       "223   0.61470   0.0   6.20     0  0.507  6.618   80.8  3.2721    8  307   \n",
       "219   0.11425   0.0  13.89     1  0.550  6.373   92.4  3.3633    5  276   \n",
       "48    0.25387   0.0   6.91     0  0.448  5.399   95.3  5.8700    3  233   \n",
       "..        ...   ...    ...   ...    ...    ...    ...     ...  ...  ...   \n",
       "88    0.05660   0.0   3.41     0  0.489  7.007   86.3  3.4217    2  270   \n",
       "466   3.77498   0.0  18.10     0  0.655  5.952   84.7  2.8715   24  666   \n",
       "52    0.05360  21.0   5.64     0  0.439  6.511   21.1  6.8147    4  243   \n",
       "121   0.07165   0.0  25.65     0  0.581  6.004   84.1  2.1974    2  188   \n",
       "218   0.11069   0.0  13.89     1  0.550  5.951   93.8  2.8893    5  276   \n",
       "\n",
       "     PTRATIO       B  LSTAT  MEDV  \n",
       "342     15.9  389.96   8.65  16.5  \n",
       "379     20.2  393.74  21.78  10.2  \n",
       "223     17.4  396.90   7.60  30.1  \n",
       "219     16.4  393.74  10.50  23.0  \n",
       "48      17.9  396.90  30.81  14.4  \n",
       "..       ...     ...    ...   ...  \n",
       "88      17.8  396.90   5.50  23.6  \n",
       "466     20.2   22.01  17.15  19.0  \n",
       "52      16.8  396.90   5.28  25.0  \n",
       "121     19.1  377.67  14.27  20.3  \n",
       "218     16.4  396.90  17.92  21.5  \n",
       "\n",
       "[102 rows x 14 columns]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strat_test_set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "1120fd32",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    95\n",
       "1     7\n",
       "Name: CHAS, dtype: int64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strat_test_set['CHAS'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "9c9f7b00",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    376\n",
       "1     28\n",
       "Name: CHAS, dtype: int64"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strat_train_set['CHAS'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "67143084",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "13.571428571428571"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "95/7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "d94f6c4a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "13.428571428571429"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "376/28"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "d8e1544f",
   "metadata": {},
   "outputs": [],
   "source": [
    "housing = strat_train_set.copy()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "636404f1",
   "metadata": {},
   "source": [
    " # Looking for Correlations\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "17bc595f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "MEDV       1.000000\n",
       "RM         0.679894\n",
       "B          0.361761\n",
       "ZN         0.339741\n",
       "DIS        0.240451\n",
       "CHAS       0.205066\n",
       "AGE       -0.364596\n",
       "RAD       -0.374693\n",
       "CRIM      -0.393715\n",
       "NOX       -0.422873\n",
       "TAX       -0.456657\n",
       "INDUS     -0.473516\n",
       "PTRATIO   -0.493534\n",
       "LSTAT     -0.740494\n",
       "Name: MEDV, dtype: float64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_matrix = housing.corr()\n",
    "corr_matrix['MEDV'].sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "86275417",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[<AxesSubplot:xlabel='MEDV', ylabel='MEDV'>,\n",
       "        <AxesSubplot:xlabel='RM', ylabel='MEDV'>,\n",
       "        <AxesSubplot:xlabel='ZN', ylabel='MEDV'>,\n",
       "        <AxesSubplot:xlabel='LSTAT', ylabel='MEDV'>],\n",
       "       [<AxesSubplot:xlabel='MEDV', ylabel='RM'>,\n",
       "        <AxesSubplot:xlabel='RM', ylabel='RM'>,\n",
       "        <AxesSubplot:xlabel='ZN', ylabel='RM'>,\n",
       "        <AxesSubplot:xlabel='LSTAT', ylabel='RM'>],\n",
       "       [<AxesSubplot:xlabel='MEDV', ylabel='ZN'>,\n",
       "        <AxesSubplot:xlabel='RM', ylabel='ZN'>,\n",
       "        <AxesSubplot:xlabel='ZN', ylabel='ZN'>,\n",
       "        <AxesSubplot:xlabel='LSTAT', ylabel='ZN'>],\n",
       "       [<AxesSubplot:xlabel='MEDV', ylabel='LSTAT'>,\n",
       "        <AxesSubplot:xlabel='RM', ylabel='LSTAT'>,\n",
       "        <AxesSubplot:xlabel='ZN', ylabel='LSTAT'>,\n",
       "        <AxesSubplot:xlabel='LSTAT', ylabel='LSTAT'>]], dtype=object)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x576 with 16 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "from pandas.plotting import scatter_matrix\n",
    "attributes = [\"MEDV\",\"RM\",\"ZN\",\"LSTAT\"]\n",
    "scatter_matrix(housing[attributes],figsize = (12,8))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "51b878f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='RM', ylabel='MEDV'>"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "housing.plot(kind = \"scatter\", x=\"RM\", y=\"MEDV\" , alpha=0.8)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c8edb043",
   "metadata": {},
   "source": [
    "## Tryingout Atribute combinations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "953daf8a",
   "metadata": {},
   "outputs": [],
   "source": [
    "housing[\"TAXRM\"] = housing['TAX']/housing['RM']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "0eaf349b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CRIM</th>\n",
       "      <th>ZN</th>\n",
       "      <th>INDUS</th>\n",
       "      <th>CHAS</th>\n",
       "      <th>NOX</th>\n",
       "      <th>RM</th>\n",
       "      <th>AGE</th>\n",
       "      <th>DIS</th>\n",
       "      <th>RAD</th>\n",
       "      <th>TAX</th>\n",
       "      <th>PTRATIO</th>\n",
       "      <th>B</th>\n",
       "      <th>LSTAT</th>\n",
       "      <th>MEDV</th>\n",
       "      <th>TAXRM</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>254</th>\n",
       "      <td>0.04819</td>\n",
       "      <td>80.0</td>\n",
       "      <td>3.64</td>\n",
       "      <td>0</td>\n",
       "      <td>0.392</td>\n",
       "      <td>6.108</td>\n",
       "      <td>32.0</td>\n",
       "      <td>9.2203</td>\n",
       "      <td>1</td>\n",
       "      <td>315</td>\n",
       "      <td>16.4</td>\n",
       "      <td>392.89</td>\n",
       "      <td>6.57</td>\n",
       "      <td>21.9</td>\n",
       "      <td>51.571709</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>348</th>\n",
       "      <td>0.01501</td>\n",
       "      <td>80.0</td>\n",
       "      <td>2.01</td>\n",
       "      <td>0</td>\n",
       "      <td>0.435</td>\n",
       "      <td>6.635</td>\n",
       "      <td>29.7</td>\n",
       "      <td>8.3440</td>\n",
       "      <td>4</td>\n",
       "      <td>280</td>\n",
       "      <td>17.0</td>\n",
       "      <td>390.94</td>\n",
       "      <td>5.99</td>\n",
       "      <td>24.5</td>\n",
       "      <td>42.200452</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>476</th>\n",
       "      <td>4.87141</td>\n",
       "      <td>0.0</td>\n",
       "      <td>18.10</td>\n",
       "      <td>0</td>\n",
       "      <td>0.614</td>\n",
       "      <td>6.484</td>\n",
       "      <td>93.6</td>\n",
       "      <td>2.3053</td>\n",
       "      <td>24</td>\n",
       "      <td>666</td>\n",
       "      <td>20.2</td>\n",
       "      <td>396.21</td>\n",
       "      <td>18.68</td>\n",
       "      <td>16.7</td>\n",
       "      <td>102.714374</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>321</th>\n",
       "      <td>0.18159</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.38</td>\n",
       "      <td>0</td>\n",
       "      <td>0.493</td>\n",
       "      <td>6.376</td>\n",
       "      <td>54.3</td>\n",
       "      <td>4.5404</td>\n",
       "      <td>5</td>\n",
       "      <td>287</td>\n",
       "      <td>19.6</td>\n",
       "      <td>396.90</td>\n",
       "      <td>6.87</td>\n",
       "      <td>23.1</td>\n",
       "      <td>45.012547</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>326</th>\n",
       "      <td>0.30347</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.38</td>\n",
       "      <td>0</td>\n",
       "      <td>0.493</td>\n",
       "      <td>6.312</td>\n",
       "      <td>28.9</td>\n",
       "      <td>5.4159</td>\n",
       "      <td>5</td>\n",
       "      <td>287</td>\n",
       "      <td>19.6</td>\n",
       "      <td>396.90</td>\n",
       "      <td>6.15</td>\n",
       "      <td>23.0</td>\n",
       "      <td>45.468948</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        CRIM    ZN  INDUS  CHAS    NOX     RM   AGE     DIS  RAD  TAX  \\\n",
       "254  0.04819  80.0   3.64     0  0.392  6.108  32.0  9.2203    1  315   \n",
       "348  0.01501  80.0   2.01     0  0.435  6.635  29.7  8.3440    4  280   \n",
       "476  4.87141   0.0  18.10     0  0.614  6.484  93.6  2.3053   24  666   \n",
       "321  0.18159   0.0   7.38     0  0.493  6.376  54.3  4.5404    5  287   \n",
       "326  0.30347   0.0   7.38     0  0.493  6.312  28.9  5.4159    5  287   \n",
       "\n",
       "     PTRATIO       B  LSTAT  MEDV       TAXRM  \n",
       "254     16.4  392.89   6.57  21.9   51.571709  \n",
       "348     17.0  390.94   5.99  24.5   42.200452  \n",
       "476     20.2  396.21  18.68  16.7  102.714374  \n",
       "321     19.6  396.90   6.87  23.1   45.012547  \n",
       "326     19.6  396.90   6.15  23.0   45.468948  "
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "housing.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "bd8b3796",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "MEDV       1.000000\n",
       "RM         0.679894\n",
       "B          0.361761\n",
       "ZN         0.339741\n",
       "DIS        0.240451\n",
       "CHAS       0.205066\n",
       "AGE       -0.364596\n",
       "RAD       -0.374693\n",
       "CRIM      -0.393715\n",
       "NOX       -0.422873\n",
       "TAX       -0.456657\n",
       "INDUS     -0.473516\n",
       "PTRATIO   -0.493534\n",
       "TAXRM     -0.525160\n",
       "LSTAT     -0.740494\n",
       "Name: MEDV, dtype: float64"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_matrix = housing.corr()\n",
    "corr_matrix['MEDV'].sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "668a6302",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='TAXRM', ylabel='MEDV'>"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "housing.plot(kind = \"scatter\", x=\"TAXRM\", y=\"MEDV\" , alpha=0.8)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b2a3f020",
   "metadata": {},
   "source": [
    "## Scikit-learn Design"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e72ed60",
   "metadata": {},
   "source": [
    "Primarily three types of objects\n",
    "\n",
    "\n",
    "1.Estimators - It estimates some parameter based on a a dataset. Eg.imputer.It has a fit method and transform method.Fit method- Fits the dataset and calculate internal parameters.\n",
    "\n",
    "\n",
    "2.Transformers - Transform method takes input and returns output based on the learning from fit().It also has a convenience function called fit_transform() which fits and then transforms.\n",
    "\n",
    "\n",
    "3.Predictors- LinearRegression model is an example of predictor. fit() and predict() are two common functions. It also gives score() function which will evaluate the predictions"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6fb2f600",
   "metadata": {},
   "source": [
    "## Feature Scaling"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c3f97385",
   "metadata": {},
   "source": [
    "Primarily, two types of features scaling methods:\n",
    "\n",
    "1. Min-max scaling (Normalization)\n",
    "    (value - min)/(max-min)\n",
    "    Sklearn provides a class called MinMaxScaler for this\n",
    "    \n",
    "    \n",
    "2. Standardization\n",
    "   (value - mean)/std\n",
    "   Sklearn provides a class called StandardScaler for this"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5bd75ec2",
   "metadata": {},
   "source": [
    "## Creating a Pipeline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "f72ad1d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "housing = strat_train_set.drop(\"MEDV\",axis=1)\n",
    "housing_labels = strat_train_set[\"MEDV\"].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "edcc2fb7",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.impute import SimpleImputer\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "my_pipeline = Pipeline([\n",
    "    ('imputer',SimpleImputer(strategy = \"median\")),\n",
    "    #.....add as many as you want in your pipeline\n",
    "    ('std_scaler',StandardScaler()),\n",
    "])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "d07c46b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "housing_num_tr = my_pipeline.fit_transform(housing)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "6e3a2d3b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(404, 13)"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "housing_num_tr.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b0dddcb9",
   "metadata": {},
   "source": [
    "## Selecting a desired model for Dragon Real Estates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "4af05a42",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>RandomForestRegressor()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">RandomForestRegressor</label><div class=\"sk-toggleable__content\"><pre>RandomForestRegressor()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "RandomForestRegressor()"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.tree import DecisionTreeRegressor\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "#model = LinearRegression()\n",
    "#model = DecisionTreeRegressor()\n",
    "model = RandomForestRegressor()\n",
    "model.fit(housing_num_tr, housing_labels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "8e1b4cc8",
   "metadata": {},
   "outputs": [],
   "source": [
    "some_data = housing.iloc[:5]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "cd3bfb06",
   "metadata": {},
   "outputs": [],
   "source": [
    "some_labels = housing_labels.iloc[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "1371989e",
   "metadata": {},
   "outputs": [],
   "source": [
    "prepared_data = my_pipeline.transform(some_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "6072ea39",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([22.508, 25.587, 16.363, 23.376, 23.391])"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.predict(prepared_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "1067b6b4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[21.9, 24.5, 16.7, 23.1, 23.0]"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(some_labels)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8fb35353",
   "metadata": {},
   "source": [
    "## Evaluating the model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "8307ba6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import mean_squared_error\n",
    "housing_predictions = model.predict(housing_num_tr)\n",
    "mse = mean_squared_error(housing_labels, housing_predictions)\n",
    "rmse= np.sqrt(mse)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "9b7c41ce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.3529252128712854"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mse"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "8b010cb9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.1631531338870584"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rmse\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6b81b6a1",
   "metadata": {},
   "source": [
    "## Using better evaluation technique- Cross Validation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "68f093b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1 2 3 4 5 6 7 8 9 10\n",
    "from sklearn.model_selection import cross_val_score\n",
    "scores = cross_val_score(model, housing_num_tr, housing_labels, scoring=\"neg_mean_squared_error\",cv=10)\n",
    "rmse_scores = np.sqrt(-scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "6391424f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2.79289168, 2.69441597, 4.40018895, 2.56972379, 3.33073436,\n",
       "       2.62687167, 4.77007351, 3.27403209, 3.38378214, 3.16691711])"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rmse_scores"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "f7b30508",
   "metadata": {},
   "outputs": [],
   "source": [
    "def print_scores(scores):\n",
    "    print(\"Scores:\",scores)\n",
    "    print(\"Mean:\",scores.mean())\n",
    "    print(\"Standard deviation: \",scores.std())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "fd1014d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Scores: [2.79289168 2.69441597 4.40018895 2.56972379 3.33073436 2.62687167\n",
      " 4.77007351 3.27403209 3.38378214 3.16691711]\n",
      "Mean: 3.3009631251857217\n",
      "Standard deviation:  0.7076841067486248\n"
     ]
    }
   ],
   "source": [
    "print_scores(rmse_scores)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a7de6a55",
   "metadata": {},
   "source": [
    "## Saving the Model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "c99e7683",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Dragon,joblib']"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from joblib import dump, load\n",
    "dump(model, 'Dragon,joblib')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1c1a4811",
   "metadata": {},
   "source": [
    "## Testing the model on test data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "50cd1f2d",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_test = strat_test_set.drop(\"MEDV\",axis=1)\n",
    "Y_test = strat_test_set[\"MEDV\"].copy()\n",
    "X_test_prepared = my_pipeline.transform(X_test)\n",
    "final_predictions = model.predict(X_test_prepared)\n",
    "final_mse = mean_squared_error(Y_test,final_predictions)\n",
    "final_rmse = np.sqrt(final_mse)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "cf7e24b2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.948844070638726"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_rmse"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "4e830d35",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-0.43942006,  3.12628155, -1.12165014, -0.27288841, -1.42262747,\n",
       "       -0.24141041, -1.31238772,  2.61111401, -1.0016859 , -0.5778192 ,\n",
       "       -0.97491834,  0.41164221, -0.86091034])"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "prepared_data[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7284e399",
   "metadata": {},
   "source": [
    "## Using the model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "54853f22",
   "metadata": {},
   "outputs": [],
   "source": [
    "from joblib import dump, load\n",
    "model = load('Dragon,joblib')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "52d1c72f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([22.508])"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "features = ([[-0.43942006,  3.12628155, -1.12165014, -0.27288841, -1.42262747,\n",
    "       -0.24141041, -1.31238772,  2.61111401, -1.0016859 , -0.5778192 ,\n",
    "       -0.97491834,  0.41164221, -0.86091034]])\n",
    "model.predict(features)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4bd1bd37",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
