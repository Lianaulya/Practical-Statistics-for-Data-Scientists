
import json, os

BASE_DATA = "https://raw.githubusercontent.com/gedeck/practical-statistics-for-data-scientists/master/data"

def nb_cell(cell_type, source, **kwargs):
    if cell_type == 'markdown':
        return {"cell_type": "markdown", "metadata": {}, "source": source if isinstance(source, list) else [source]}
    else:
        return {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": source if isinstance(source, list) else [source]
        }

def notebook(cells, kernel='python3'):
    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11.0"}
        },
        "cells": cells
    }

# ─────────────────────────────────────────────────────────────────────────────
# CHAPTER 1 – Exploratory Data Analysis
# ─────────────────────────────────────────────────────────────────────────────
ch1_cells = [
    nb_cell('markdown', [
        '<a href="https://colab.research.google.com/github/Lianaulya/Practical-Statistics-for-Data-Scientists/'
        'blob/main/Chapter1_EDA.ipynb" target="_parent">'
        '<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'
    ]),
    nb_cell('markdown', ['# Chapter 1 – Exploratory Data Analysis\n',
        '**Book:** *Practical Statistics for Data Scientists* (O\'Reilly)\n\n',
        'This notebook reproduces the key concepts and code examples from Chapter 1:\n',
        '- Estimates of location (mean, median, trimmed mean, weighted mean)\n',
        '- Estimates of variability (std dev, MAD, IQR)\n',
        '- Percentiles & Box Plots\n',
        '- Frequency Tables & Histograms\n',
        '- Density Plots\n',
        '- Binary & Categorical Data\n',
        '- Scatterplots & Correlation\n'
    ]),
    nb_cell('code', [
        '# Install required packages (run once)\n',
        '# !pip install wquantiles'
    ]),
    nb_cell('code', [
        '%matplotlib inline\n\n',
        'import numpy as np\n',
        'import pandas as pd\n',
        'import matplotlib.pyplot as plt\n',
        'import seaborn as sns\n',
        'from scipy import stats\n',
        'import wquantiles\n\n',
        'BASE_DATA = "https://raw.githubusercontent.com/gedeck/practical-statistics-for-data-scientists/master/data"\n',
        'print("Libraries loaded successfully!")'
    ]),
    nb_cell('markdown', [
        '## 1. Estimates of Location\n\n',
        '### Mean (Average)\n',
        'The **mean** is the most basic measure of central location:\n\n',
        r'$$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$' + '\n\n',
        '### Median\n',
        'The **median** is the middle value when data is sorted – it is robust to outliers.\n\n',
        '### Trimmed Mean\n',
        'A **trimmed mean** removes a fixed proportion of the smallest and largest values before computing the average.\n',
        'This reduces the effect of extreme outliers.\n\n',
        '### Weighted Mean\n',
        r'$$\bar{x}_w = \frac{\sum_{i=1}^{n} w_i x_i}{\sum_{i=1}^{n} w_i}$$'
    ]),
    nb_cell('code', [
        '# Table 1-2: State population and murder rate data\n',
        'state = pd.read_csv(f"{BASE_DATA}/state.csv")\n',
        'print(state.head(8))'
    ]),
    nb_cell('code', [
        '# Mean, trimmed mean (10%), weighted mean\n',
        'mean_pop = state["Population"].mean()\n',
        'trimmed_mean = stats.trim_mean(state["Population"], 0.1)\n',
        'weighted_mean = np.average(state["Murder.Rate"], weights=state["Population"])\n\n',
        'print(f"Mean Population:         {mean_pop:,.0f}")\n',
        'print(f"Trimmed Mean (10%):      {trimmed_mean:,.0f}")\n',
        'print(f"Weighted Mean (Murder):  {weighted_mean:.4f}")\n\n',
        '# Median\n',
        'print(f"Median Population:       {state[\'Population\'].median():,.0f}")'
    ]),
    nb_cell('markdown', [
        '## 2. Estimates of Variability\n\n',
        '### Variance and Standard Deviation\n',
        r'$$s = \sqrt{\frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}}$$' + '\n\n',
        '### Mean Absolute Deviation (MAD)\n',
        r'$$MAD = \frac{\sum_{i=1}^{n}|x_i - \bar{x}|}{n}$$' + '\n\n',
        '### Median Absolute Deviation from Median\n',
        r'$$Median\;MAD = Median(|x_i - m|)$$ where $m$ is the median.\n\n',
        '### Percentiles & IQR\n',
        r'$$IQR = Q_3 - Q_1$$' + ' (75th percentile − 25th percentile)'
    ]),
    nb_cell('code', [
        '# Variability estimates\n',
        'pop = state["Population"]\n\n',
        'print(f"Standard Deviation:   {pop.std():,.0f}")\n',
        'print(f"IQR:                  {pop.quantile(0.75) - pop.quantile(0.25):,.0f}")\n',
        'print(f"MAD:                  {(pop - pop.mean()).abs().mean():,.0f}")\n',
        'print(f"Median Abs Dev:       {(pop - pop.median()).abs().median():,.0f}")'
    ]),
    nb_cell('markdown', ['## 3. Percentiles and Box Plots\n\n',
        'Percentiles partition the data into 100 equal parts. The **box plot** visualizes the five-number summary:\n',
        '- Minimum (or 5th percentile)\n',
        '- Q1 (25th percentile)\n',
        '- Median (50th percentile)\n',
        '- Q3 (75th percentile)\n',
        '- Maximum (or 95th percentile)\n'
    ]),
    nb_cell('code', [
        '# Percentiles of murder rate\n',
        'percentiles = [5, 25, 50, 75, 95]\n',
        'print("Percentiles of Murder Rate:")\n',
        'for p in percentiles:\n',
        '    print(f"  P{p:2d}: {state[\'Murder.Rate\'].quantile(p/100):.2f}")'
    ]),
    nb_cell('code', [
        '# Box plot of population by region\n',
        'fig, ax = plt.subplots(figsize=(8, 4))\n',
        'state.boxplot("Population", ax=ax)\n',
        'ax.set_title("Population Distribution Across US States")\n',
        'ax.set_ylabel("Population")\n',
        'ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x/1e6:.1f}M"))\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ['## 4. Frequency Tables and Histograms\n\n',
        'A **frequency table** bins continuous data into discrete intervals and counts how many observations fall in each bin.\n',
        'A **histogram** is the graphical version of a frequency table.'
    ]),
    nb_cell('code', [
        '# Frequency table of murder rates\n',
        'bins = [1, 2.5, 4, 5.5, 7, 9, 11]\n',
        'freq, edges = np.histogram(state["Murder.Rate"], bins=bins)\n',
        'freq_df = pd.DataFrame({"BinStart": edges[:-1], "BinEnd": edges[1:], "Count": freq})\n',
        'print("Murder Rate Frequency Table:")\n',
        'print(freq_df.to_string(index=False))'
    ]),
    nb_cell('code', [
        '# Histogram of murder rate\n',
        'fig, ax = plt.subplots(figsize=(8, 4))\n',
        'state["Murder.Rate"].hist(bins=bins, ax=ax, edgecolor="black", color="steelblue")\n',
        'ax.set_title("Histogram of State Murder Rates")\n',
        'ax.set_xlabel("Murder Rate (per 100,000)")\n',
        'ax.set_ylabel("Frequency")\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('code', [
        '# DFW airline delays — bar chart\n',
        'dfw = pd.read_csv(f"{BASE_DATA}/dfw_airline.csv")\n',
        'print(dfw.head())\n\n',
        'fig, ax = plt.subplots(figsize=(9, 4))\n',
        'dfw.transpose().plot(kind="bar", ax=ax, legend=False, color="steelblue", edgecolor="black")\n',
        'ax.set_title("DFW Airport – % Delayed Flights by Airline")\n',
        'ax.set_xlabel("Airline")\n',
        'ax.set_ylabel("% of Delays")\n',
        'plt.xticks(rotation=45, ha="right")\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ['## 5. Density Plots and Estimates\n\n',
        'A **density plot** (KDE – Kernel Density Estimate) is a smoothed version of a histogram.\n',
        'It shows the *shape* of the distribution without being sensitive to bin choice.\n\n',
        'KDE uses a smoothing kernel $K$ with bandwidth $h$:\n\n',
        r'$$\hat{f}(x) = \frac{1}{nh} \sum_{i=1}^{n} K\!\left(\frac{x - x_i}{h}\right)$$'
    ]),
    nb_cell('code', [
        '# KDE / density of murder rate\n',
        'fig, axes = plt.subplots(1, 2, figsize=(12, 4))\n\n',
        '# Histogram + KDE\n',
        'state["Murder.Rate"].plot.hist(bins=10, density=True, ax=axes[0], color="lightsteelblue", edgecolor="black")\n',
        'state["Murder.Rate"].plot.kde(ax=axes[0], color="navy")\n',
        'axes[0].set_title("Murder Rate – Histogram + KDE")\n',
        'axes[0].set_xlabel("Murder Rate")\n\n',
        '# Pure KDE\n',
        'state["Murder.Rate"].plot.kde(ax=axes[1], color="steelblue", linewidth=2)\n',
        'axes[1].set_title("Murder Rate – Kernel Density Estimate")\n',
        'axes[1].set_xlabel("Murder Rate")\n\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ['## 6. Exploring Binary and Categorical Data\n\n',
        'For binary (0/1) or categorical data we summarize using:\n',
        '- **Proportions / mode** for categorical\n',
        '- **Expected value**: $E(X) = \\sum_{i} x_i \\cdot P(x_i)$\n',
        '- **Bar charts** for visualization'
    ]),
    nb_cell('code', [
        '# Lending Club loans — categorical counts\n',
        'lc_loans = pd.read_csv(f"{BASE_DATA}/lc_loans.csv")\n',
        'print(lc_loans["status"].value_counts())\n',
        'print("\\nProportions:")\n',
        'print(lc_loans["status"].value_counts(normalize=True).round(3))'
    ]),
    nb_cell('code', [
        '# Stacked bar chart by status and term\n',
        'pivot = lc_loans.pivot_table(index="grade", columns="status", values="amount",\n',
        '                              aggfunc="sum", fill_value=0)\n',
        'fig, ax = plt.subplots(figsize=(10, 5))\n',
        'pivot.plot(kind="bar", stacked=True, ax=ax, colormap="tab10")\n',
        'ax.set_title("Loan Amount by Grade and Status")\n',
        'ax.set_xlabel("Grade")\n',
        'ax.set_ylabel("Total Amount ($)")\n',
        'ax.legend(title="Status", bbox_to_anchor=(1.01, 1))\n',
        'plt.xticks(rotation=0)\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ['## 7. Correlation\n\n',
        'The **Pearson correlation coefficient** measures linear association:\n\n',
        r'$$r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{(n-1)\,s_x s_y}$$' + '\n\n',
        '- $r = 1$: perfect positive linear correlation\n',
        '- $r = -1$: perfect negative linear correlation\n',
        '- $r = 0$: no linear correlation\n'
    ]),
    nb_cell('code', [
        '# S&P 500 sector correlations\n',
        'sp500_sym = pd.read_csv(f"{BASE_DATA}/sp500_sectors.csv")\n',
        'sp500_px = pd.read_csv(f"{BASE_DATA}/sp500_data.csv.gz", index_col=0)\n',
        'print("S&P500 data shape:", sp500_px.shape)\n',
        'print(sp500_sym.head())'
    ]),
    nb_cell('code', [
        '# Compute telecom sector correlations\n',
        'telecom = sp500_sym[sp500_sym["sector"] == "telecommunications_services"]["symbol"]\n',
        'telecom_px = sp500_px[telecom]\n',
        'corr_matrix = telecom_px.corr()\n\n',
        'fig, ax = plt.subplots(figsize=(7, 6))\n',
        'sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm",\n',
        '            center=0, ax=ax, square=True)\n',
        'ax.set_title("Telecom Sector – Return Correlations")\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ['## 8. Scatterplots\n\n',
        'A **scatterplot** shows the relationship between two continuous variables.\n',
        'We can use alpha blending and hexbin for large datasets.'
    ]),
    nb_cell('code', [
        '# King County, WA – Tax assessed value vs. finished sqft\n',
        'kc_tax = pd.read_csv(f"{BASE_DATA}/kc_tax.csv.gz")\n',
        'kc_tax = kc_tax.dropna()\n',
        'kc_tax = kc_tax[(kc_tax["TaxAssessedValue"] < 750000) &\n',
        '                (kc_tax["SqFtTotLiving"] < 3500) &\n',
        '                (kc_tax["SqFtTotLiving"] > 300)]\n',
        'print(f"KC Tax data: {kc_tax.shape[0]:,} rows after filtering")'
    ]),
    nb_cell('code', [
        '# Hexbin scatterplot for large dataset\n',
        'fig, ax = plt.subplots(figsize=(8, 5))\n',
        'kc_tax.plot.hexbin("SqFtTotLiving", "TaxAssessedValue",\n',
        '                   gridsize=30, sharex=False, ax=ax,\n',
        '                   colormap="Blues", edgecolors="none")\n',
        'ax.set_title("KC Tax Value vs. Living Area")\n',
        'ax.set_xlabel("Square Feet (Total Living)")\n',
        'ax.set_ylabel("Tax Assessed Value ($)")\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ['## Summary\n\n',
        '| Concept | Key Formula / Tool |\n',
        '|---------|-------------------|\n',
        r'| Mean | $\bar{x} = \frac{\sum x_i}{n}$ |' + '\n',
        r'| Trimmed Mean | Remove top/bottom $p\%$, then average |' + '\n',
        r'| Weighted Mean | $\frac{\sum w_i x_i}{\sum w_i}$ |' + '\n',
        r'| Std Deviation | $s = \sqrt{\frac{\sum(x_i-\bar{x})^2}{n-1}}$ |' + '\n',
        r'| IQR | $Q_3 - Q_1$ |' + '\n',
        r'| Pearson Corr | $r \in [-1, 1]$ |' + '\n',
    ])
]

# ─────────────────────────────────────────────────────────────────────────────
# CHAPTER 2 – Data and Sampling Distributions
# ─────────────────────────────────────────────────────────────────────────────
ch2_cells = [
    nb_cell('markdown', [
        '<a href="https://colab.research.google.com/github/Lianaulya/Practical-Statistics-for-Data-Scientists/'
        'blob/main/Chapter2_SamplingDistributions.ipynb" target="_parent">'
        '<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'
    ]),
    nb_cell('markdown', ['# Chapter 2 – Data and Sampling Distributions\n',
        '**Book:** *Practical Statistics for Data Scientists* (O\'Reilly)\n\n',
        'Topics covered:\n',
        '- Random Sampling & Sample Bias\n',
        '- Sampling Distribution of a Statistic\n',
        '- The Bootstrap\n',
        '- Confidence Intervals\n',
        '- Normal Distribution\n',
        '- Long-Tailed Distributions\n',
        '- Student\'s t-Distribution\n',
        '- Binomial Distribution\n',
        '- Poisson Distribution\n'
    ]),
    nb_cell('code', [
        '%matplotlib inline\n\n',
        'import numpy as np\n',
        'import pandas as pd\n',
        'import matplotlib.pyplot as plt\n',
        'import seaborn as sns\n',
        'from scipy import stats\n\n',
        'BASE_DATA = "https://raw.githubusercontent.com/gedeck/practical-statistics-for-data-scientists/master/data"\n',
        'print("Libraries loaded successfully!")'
    ]),
    nb_cell('markdown', ['## 1. Random Sampling\n\n',
        'A **simple random sample** gives every element an equal probability of selection.\n',
        'Key concern: **sample bias** – when some members are systematically more/less likely to be selected.\n\n',
        '**Stratified sampling** divides the population into sub-groups (strata) and samples from each.\n',
        '**Cluster sampling** randomly selects entire groups (clusters).'
    ]),
    nb_cell('code', [
        '# Loans income data\n',
        'loans_income = pd.read_csv(f"{BASE_DATA}/loans_income.csv", squeeze=True)\n\n',
        'print(f"Population size: {len(loans_income):,}")\n',
        'print(f"Population Mean: ${loans_income.mean():,.2f}")\n',
        'print(f"Population Std:  ${loans_income.std():,.2f}")'
    ]),
    nb_cell('code', [
        '# Take a random sample of 1000\n',
        'np.random.seed(42)\n',
        'sample = loans_income.sample(1000)\n',
        'print(f"Sample Mean:  ${sample.mean():,.2f}")\n',
        'print(f"Sample Std:   ${sample.std():,.2f}")\n',
        'print(f"Error in mean: ${abs(sample.mean() - loans_income.mean()):,.2f}")'
    ]),
    nb_cell('markdown', ['## 2. Sampling Distribution of a Statistic\n\n',
        'The **sampling distribution** of a statistic (e.g., the sample mean) describes how that\n',
        'statistic varies from sample to sample.\n\n',
        '**Central Limit Theorem (CLT)**: As sample size $n$ increases, the sampling distribution\n',
        'of the mean approaches a normal distribution:\n\n',
        r'$$\bar{X} \sim \mathcal{N}\!\left(\mu,\; \frac{\sigma^2}{n}\right)$$' + '\n\n',
        '**Standard Error** of the mean: $SE = \\dfrac{\\sigma}{\\sqrt{n}}$'
    ]),
    nb_cell('code', [
        '# Demonstrate CLT: sample means from 1000 repetitions\n',
        'np.random.seed(42)\n',
        'sample_means_5  = [loans_income.sample(5).mean() for _ in range(1000)]\n',
        'sample_means_20 = [loans_income.sample(20).mean() for _ in range(1000)]\n',
        'sample_means_100= [loans_income.sample(100).mean() for _ in range(1000)]\n\n',
        'fig, axes = plt.subplots(1, 3, figsize=(14, 4))\n',
        'for ax, means, n in zip(axes, [sample_means_5, sample_means_20, sample_means_100], [5, 20, 100]):\n',
        '    pd.Series(means).hist(bins=30, ax=ax, color="steelblue", edgecolor="black")\n',
        '    ax.set_title(f"n = {n} | SE = ${np.std(means):,.0f}")\n',
        '    ax.set_xlabel("Sample Mean Income ($)")\n',
        'axes[0].set_ylabel("Frequency")\n',
        'fig.suptitle("Central Limit Theorem – Sampling Distribution of the Mean", y=1.02)\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ['## 3. The Bootstrap\n\n',
        'The **bootstrap** is a resampling technique that estimates the sampling distribution\n',
        'of a statistic by repeatedly resampling *with replacement* from the original data:\n\n',
        '1. Draw $B$ bootstrap samples of size $n$ (with replacement)\n',
        '2. Compute the statistic $\\hat{\\theta}^*_b$ for each sample\n',
        '3. The distribution of $\\hat{\\theta}^*_b$ approximates the sampling distribution\n\n',
        'Bootstrap standard error: $SE_{boot} = \\sqrt{\\dfrac{1}{B-1}\\sum_{b=1}^B (\\hat{\\theta}^*_b - \\bar{\\theta}^*)^2}$'
    ]),
    nb_cell('code', [
        '# Bootstrap estimation of the median income\n',
        'np.random.seed(42)\n',
        'sample_data = loans_income.sample(1000)\n\n',
        'n_boot = 1000\n',
        'bootstrap_medians = [\n',
        '    sample_data.sample(len(sample_data), replace=True).median()\n',
        '    for _ in range(n_boot)\n',
        ']\n\n',
        'boot_se = np.std(bootstrap_medians)\n',
        'boot_ci_lo = np.percentile(bootstrap_medians, 2.5)\n',
        'boot_ci_hi = np.percentile(bootstrap_medians, 97.5)\n\n',
        'print(f"Sample Median:        ${sample_data.median():,.2f}")\n',
        'print(f"Bootstrap SE:         ${boot_se:,.2f}")\n',
        'print(f"95% CI:               [${boot_ci_lo:,.2f}, ${boot_ci_hi:,.2f}]")\n\n',
        'fig, ax = plt.subplots(figsize=(8, 4))\n',
        'pd.Series(bootstrap_medians).hist(bins=30, ax=ax, color="steelblue", edgecolor="black")\n',
        'ax.axvline(boot_ci_lo, color="red", linestyle="--", label="2.5th pctile")\n',
        'ax.axvline(boot_ci_hi, color="red", linestyle="-.", label="97.5th pctile")\n',
        'ax.set_title("Bootstrap Distribution of Median Income")\n',
        'ax.set_xlabel("Median Income ($)")\n',
        'ax.legend()\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ['## 4. Confidence Intervals\n\n',
        'A **confidence interval** (CI) provides a range of plausible values for the population parameter.\n',
        'A 95% CI means: if we repeated the sampling process many times, 95% of the resulting CIs\n',
        'would contain the true parameter.\n\n',
        'For large samples using the CLT:\n\n',
        r'$$\text{95% CI} = \bar{x} \pm 1.96 \cdot \frac{s}{\sqrt{n}}$$'
    ]),
    nb_cell('code', [
        '# Confidence intervals via bootstrap (already computed above)\n',
        '# Let us also compute the formula-based CI for the mean\n\n',
        'n = len(sample_data)\n',
        'x_bar = sample_data.mean()\n',
        'se = sample_data.std() / np.sqrt(n)\n',
        'ci_low  = x_bar - 1.96 * se\n',
        'ci_high = x_bar + 1.96 * se\n\n',
        'print(f"Formula-based 95% CI for Mean Income:")\n',
        'print(f"  Mean:  ${x_bar:,.2f}")\n',
        'print(f"  SE:    ${se:,.2f}")\n',
        'print(f"  Lower: ${ci_low:,.2f}")\n',
        'print(f"  Upper: ${ci_high:,.2f}")'
    ]),
    nb_cell('markdown', ['## 5. Normal Distribution\n\n',
        'The **normal (Gaussian) distribution** is defined by:\n\n',
        r'$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$' + '\n\n',
        'Key properties:\n',
        '- Symmetric around $\\mu$\n',
        '- 68% of data within $\\mu \\pm 1\\sigma$\n',
        '- 95% within $\\mu \\pm 2\\sigma$\n',
        '- 99.7% within $\\mu \\pm 3\\sigma$ (empirical rule)\n\n',
        '**Standardization / Z-score**: $z = \\dfrac{x - \\mu}{\\sigma}$'
    ]),
    nb_cell('code', [
        '# QQ-plot: check normality of income sample\n',
        'fig, axes = plt.subplots(1, 2, figsize=(12, 4))\n\n',
        'sample_data.hist(bins=30, ax=axes[0], color="steelblue", edgecolor="black", density=True)\n',
        'x = np.linspace(sample_data.min(), sample_data.max(), 200)\n',
        'axes[0].plot(x, stats.norm.pdf(x, sample_data.mean(), sample_data.std()),\n',
        '             "r-", linewidth=2, label="Normal PDF")\n',
        'axes[0].set_title("Loan Income – Histogram vs. Normal")\n',
        'axes[0].set_xlabel("Income ($)")\n',
        'axes[0].legend()\n\n',
        '# QQ plot\n',
        'stats.probplot(sample_data, dist="norm", plot=axes[1])\n',
        'axes[1].set_title("Q-Q Plot")\n\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ['## 6. Long-Tailed Distributions\n\n',
        'Not all data is normally distributed. **Long-tailed** (or heavy-tailed) distributions\n',
        'have more probability in the tails than the normal distribution.\n\n',
        'Examples: income, stock returns, city populations (power-law tails).\n',
        '**Skewness** measures the asymmetry; **kurtosis** measures tail heaviness.'
    ]),
    nb_cell('code', [
        '# S&P 500 returns — check for fat tails\n',
        'sp500_px = pd.read_csv(f"{BASE_DATA}/sp500_data.csv.gz", index_col=0)\n',
        'sp500_returns = sp500_px.pct_change().dropna()\n\n',
        '# Take Apple as example\n',
        'aapl = sp500_returns["AAPL"]\n',
        'print(f"AAPL Returns — Skewness: {aapl.skew():.4f}, Kurtosis: {aapl.kurtosis():.4f}")\n\n',
        'fig, ax = plt.subplots(figsize=(9, 4))\n',
        'aapl.hist(bins=60, ax=ax, color="steelblue", edgecolor="black", density=True)\n',
        'x = np.linspace(aapl.min(), aapl.max(), 200)\n',
        'ax.plot(x, stats.norm.pdf(x, aapl.mean(), aapl.std()), "r-", linewidth=2, label="Normal")\n',
        'ax.set_title("AAPL Daily Returns — Heavy Tails vs. Normal")\n',
        'ax.set_xlabel("Daily Return")\n',
        'ax.legend()\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ["## 7. Student's t-Distribution\n\n",
        "When the population variance is **unknown** and the sample size is small, we use Student's **t-distribution**:\n\n",
        r'$$t = \frac{\bar{X} - \mu}{s/\sqrt{n}}$$' + '\n\n',
        'with $n-1$ degrees of freedom. As $n \\to \\infty$, the t-distribution converges to the normal.'
    ]),
    nb_cell('code', [
        '# Compare t vs. normal for different degrees of freedom\n',
        'x = np.linspace(-4, 4, 200)\n',
        'fig, ax = plt.subplots(figsize=(9, 4))\n',
        'ax.plot(x, stats.norm.pdf(x), "k-", linewidth=2, label="Normal")\n',
        'for df, col in [(1, "red"), (3, "orange"), (10, "steelblue"), (30, "green")]:\n',
        '    ax.plot(x, stats.t.pdf(x, df), linestyle="--", label=f"t (df={df})", color=col)\n',
        'ax.set_title("t-Distribution vs. Normal — Heavier Tails for Small df")\n',
        'ax.set_xlabel("Value")\n',
        'ax.set_ylabel("Density")\n',
        'ax.legend()\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ['## 8. Binomial Distribution\n\n',
        'The **binomial distribution** counts successes in $n$ independent Bernoulli trials,\n',
        'each with success probability $p$:\n\n',
        r'$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$' + '\n\n',
        r'Mean: $\mu = np$ &emsp; Variance: $\sigma^2 = np(1-p)$'
    ]),
    nb_cell('code', [
        '# Binomial example: click-through rate\n',
        'n, p = 200, 0.05  # 200 visitors, 5% click rate\n',
        'k = np.arange(0, 26)\n',
        'probs = stats.binom.pmf(k, n, p)\n\n',
        'fig, ax = plt.subplots(figsize=(9, 4))\n',
        'ax.bar(k, probs, color="steelblue", edgecolor="black", alpha=0.7)\n',
        'ax.set_title(f"Binomial Distribution — n={n}, p={p}")\n',
        'ax.set_xlabel("Number of Successes")\n',
        'ax.set_ylabel("Probability")\n',
        'ax.axvline(n * p, color="red", linestyle="--", label=f"Mean = {n*p}")\n',
        'ax.legend()\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ['## 9. Poisson Distribution\n\n',
        'The **Poisson distribution** models the number of events in a fixed time interval,\n',
        'given a known average rate $\\lambda$:\n\n',
        r'$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$' + '\n\n',
        r'Mean $= \lambda$, Variance $= \lambda$'
    ]),
    nb_cell('code', [
        '# Poisson example: server requests per second\n',
        'lambda_ = 7  # average 7 requests per second\n',
        'k = np.arange(0, 21)\n',
        'probs_pois = stats.poisson.pmf(k, lambda_)\n\n',
        'fig, ax = plt.subplots(figsize=(9, 4))\n',
        'ax.bar(k, probs_pois, color="coral", edgecolor="black", alpha=0.8)\n',
        'ax.set_title(f"Poisson Distribution — λ = {lambda_} events/sec")\n',
        'ax.set_xlabel("Number of Events (k)")\n',
        'ax.set_ylabel("Probability")\n',
        'ax.axvline(lambda_, color="navy", linestyle="--", label=f"Mean = {lambda_}")\n',
        'ax.legend()\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ['## Summary\n\n',
        '| Concept | Key Point |\n',
        '|---------|----------|\n',
        '| CLT | Sample mean → Normal as $n$ grows |\n',
        '| SE | $\\sigma / \\sqrt{n}$ — precision of the sample mean |\n',
        '| Bootstrap | Resampling to estimate sampling distribution |\n',
        '| 95% CI | $\\bar{x} \\pm 1.96 \\cdot SE$ |\n',
        '| t-dist | Heavier tails than Normal; used when $\\sigma$ unknown |\n',
        '| Binomial | Count of successes in $n$ Bernoulli trials |\n',
        '| Poisson | Count of events in fixed interval with rate $\\lambda$ |\n',
    ])
]

# ─────────────────────────────────────────────────────────────────────────────
# CHAPTER 3 – Statistical Experiments and Significance Testing
# ─────────────────────────────────────────────────────────────────────────────
ch3_cells = [
    nb_cell('markdown', [
        '<a href="https://colab.research.google.com/github/Lianaulya/Practical-Statistics-for-Data-Scientists/'
        'blob/main/Chapter3_StatisticalExperiments.ipynb" target="_parent">'
        '<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'
    ]),
    nb_cell('markdown', ['# Chapter 3 – Statistical Experiments and Significance Testing\n',
        '**Book:** *Practical Statistics for Data Scientists* (O\'Reilly)\n\n',
        'Topics:\n',
        '- A/B Testing\n',
        '- Hypothesis Tests (p-values, null hypothesis)\n',
        '- Resampling Permutation Tests\n',
        '- t-Tests\n',
        '- Multiple Testing\n',
        '- ANOVA and F-statistics\n',
        '- Chi-Square Test\n',
        '- Power & Sample Size\n'
    ]),
    nb_cell('code', [
        '%matplotlib inline\n\n',
        'import numpy as np\n',
        'import pandas as pd\n',
        'import matplotlib.pyplot as plt\n',
        'import seaborn as sns\n',
        'from scipy import stats\n\n',
        'BASE_DATA = "https://raw.githubusercontent.com/gedeck/practical-statistics-for-data-scientists/master/data"\n',
        'print("Libraries loaded!")'
    ]),
    nb_cell('markdown', ['## 1. A/B Testing\n\n',
        'An **A/B test** (controlled experiment) compares two versions of something (A and B)\n',
        'to determine which performs better.\n\n',
        '**Procedure:**\n',
        '1. Define a clear metric (conversion rate, click-through rate, etc.)\n',
        '2. Randomly assign subjects to group A (control) and B (treatment)\n',
        '3. Run the experiment and collect data\n',
        '4. Test whether the observed difference is statistically significant\n\n',
        '**Null hypothesis $H_0$**: There is no difference between A and B.\n',
        '**Alternative hypothesis $H_a$**: There is a difference.\n'
    ]),
    nb_cell('code', [
        '# A/B Test — web page session times\n',
        'session_times = pd.read_csv(f"{BASE_DATA}/web_page_data.csv")\n',
        'session_times.columns = ["Page", "Time"]\n',
        'print(session_times.groupby("Page")["Time"].describe())'
    ]),
    nb_cell('code', [
        '# Visualise group distributions\n',
        'fig, axes = plt.subplots(1, 2, figsize=(12, 4))\n\n',
        'for ax, page, color in zip(axes, ["Page A", "Page B"], ["steelblue", "coral"]):\n',
        '    data = session_times[session_times["Page"] == page]["Time"]\n',
        '    data.hist(bins=20, ax=ax, color=color, edgecolor="black")\n',
        '    ax.axvline(data.mean(), color="black", linestyle="--",\n',
        '               label=f"Mean = {data.mean():.1f}s")\n',
        '    ax.set_title(f"{page} – Session Time")\n',
        '    ax.set_xlabel("Time (seconds)")\n',
        '    ax.legend()\n\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ['## 2. Hypothesis Tests and P-values\n\n',
        'The **p-value** is the probability of observing a result at least as extreme as\n',
        'the observed statistic, **assuming the null hypothesis is true**.\n\n',
        '- If $p < \\alpha$ (usually 0.05): reject $H_0$ → "statistically significant"\n',
        '- If $p \\geq \\alpha$: fail to reject $H_0$\n\n',
        '> **Caution:** A small p-value does not imply practical significance. Always check effect size!'
    ]),
    nb_cell('code', [
        '# Permutation test for A/B session times\n',
        'page_a = session_times[session_times["Page"] == "Page A"]["Time"].values\n',
        'page_b = session_times[session_times["Page"] == "Page B"]["Time"].values\n\n',
        'observed_diff = page_b.mean() - page_a.mean()\n',
        'print(f"Observed difference (B - A): {observed_diff:.4f} seconds")\n\n',
        'np.random.seed(42)\n',
        'combined = np.concatenate([page_a, page_b])\n',
        'n_a = len(page_a)\n',
        'permutation_diffs = []\n',
        'for _ in range(2000):\n',
        '    perm = np.random.permutation(combined)\n',
        '    permutation_diffs.append(perm[n_a:].mean() - perm[:n_a].mean())\n\n',
        'p_value = np.mean(np.abs(permutation_diffs) >= np.abs(observed_diff))\n',
        'print(f"Permutation p-value: {p_value:.4f}")'
    ]),
    nb_cell('code', [
        '# Visualize permutation distribution\n',
        'fig, ax = plt.subplots(figsize=(9, 4))\n',
        'pd.Series(permutation_diffs).hist(bins=40, ax=ax, color="steelblue", edgecolor="black")\n',
        'ax.axvline(observed_diff, color="red", linewidth=2, label=f"Observed diff = {observed_diff:.3f}")\n',
        'ax.axvline(-observed_diff, color="orange", linewidth=2, linestyle="--")\n',
        'ax.set_title("Permutation Distribution – H₀: No difference between pages")\n',
        'ax.set_xlabel("Difference in Means (B − A)")\n',
        'ax.legend()\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ['## 3. t-Test\n\n',
        'The **two-sample t-test** tests whether the means of two groups differ:\n\n',
        r'$$t = \frac{\bar{X}_A - \bar{X}_B}{\sqrt{\frac{s_A^2}{n_A} + \frac{s_B^2}{n_B}}}$$' + '\n\n',
        'With Welch correction for unequal variances.'
    ]),
    nb_cell('code', [
        '# Two-sample t-test\n',
        't_stat, p_val = stats.ttest_ind(page_b, page_a, equal_var=False)\n',
        'print(f"t-statistic: {t_stat:.4f}")\n',
        'print(f"p-value:     {p_val:.4f}")\n',
        'print(f"Conclusion:  {\'Reject H₀\' if p_val < 0.05 else \'Fail to reject H₀\'}")'
    ]),
    nb_cell('markdown', ['## 4. ANOVA and F-Statistic\n\n',
        'Analysis of Variance (**ANOVA**) tests whether the means of **3+ groups** differ.\n\n',
        r'$$F = \frac{\text{Between-group variance (MSB)}}{\text{Within-group variance (MSW)}}$$' + '\n\n',
        'Large $F$ → evidence against $H_0$ (that all group means are equal).'
    ]),
    nb_cell('code', [
        '# ANOVA: web page session times across four sessions\n',
        'four_sessions = pd.read_csv(f"{BASE_DATA}/four_sessions.csv")\n',
        'print(four_sessions.head())\n',
        'print("\\nGroup means:")\n',
        'print(four_sessions.groupby("Page")["Time"].mean())'
    ]),
    nb_cell('code', [
        '# One-way ANOVA\n',
        'groups = [group["Time"].values for _, group in four_sessions.groupby("Page")]\n',
        'f_stat, p_val = stats.f_oneway(*groups)\n',
        'print(f"F-statistic: {f_stat:.4f}")\n',
        'print(f"p-value:     {p_val:.4f}")\n',
        'print(f"Conclusion:  {\'Reject H₀\' if p_val < 0.05 else \'Fail to reject H₀\'}")\n\n',
        '# Box plot of groups\n',
        'fig, ax = plt.subplots(figsize=(8, 4))\n',
        'four_sessions.boxplot("Time", by="Page", ax=ax)\n',
        'ax.set_title("Session Time by Page Version")\n',
        'ax.set_xlabel("Page")\n',
        'ax.set_ylabel("Time (seconds)")\n',
        'plt.suptitle("")\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ['## 5. Chi-Square Test\n\n',
        'The **chi-square test** checks whether categorical variables are independent:\n\n',
        r'$$\chi^2 = \sum_i \frac{(O_i - E_i)^2}{E_i}$$' + '\n\n',
        'where $O_i$ = observed, $E_i$ = expected count under independence.'
    ]),
    nb_cell('code', [
        '# Chi-square test: click-through rates by headline\n',
        'click_rate = pd.read_csv(f"{BASE_DATA}/click_rates.csv")\n',
        'print(click_rate)'
    ]),
    nb_cell('code', [
        '# Contingency table and chi-square test\n',
        'contingency = click_rate.pivot_table(index="Headline", columns="Click", values="Rate")\n',
        'contingency = click_rate.groupby("Headline")["Rate"].sum().reset_index()\n\n',
        '# Simple chi-square on the click-rate table\n',
        'pivot = click_rate.pivot_table(index="Headline", columns="Click", values="Rate", fill_value=0)\n',
        'chi2, p, dof, expected = stats.chi2_contingency(pivot.values)\n',
        'print(f"Chi-square statistic: {chi2:.4f}")\n',
        'print(f"p-value:              {p:.4f}")\n',
        'print(f"Degrees of freedom:   {dof}")'
    ]),
    nb_cell('markdown', ['## 6. Power and Sample Size\n\n',
        '**Statistical power** (1 − β) is the probability of correctly rejecting $H_0$ when it is false.\n\n',
        'Key relationships:\n',
        '- Higher power → need larger sample size\n',
        '- Smaller effect size → need larger sample size\n',
        '- Smaller $\\alpha$ → need larger sample size\n\n',
        'Minimum sample size per group (two-sample t-test):\n\n',
        r'$$n \approx \frac{2\sigma^2 (z_{\alpha/2} + z_{\beta})^2}{\delta^2}$$'
    ]),
    nb_cell('code', [
        '# Power analysis: what sample size for 80% power?\n',
        'from scipy.stats import norm\n\n',
        'alpha = 0.05\n',
        'power = 0.80\n',
        'effect_size = 0.3  # standard deviations\n\n',
        'z_alpha2 = norm.ppf(1 - alpha/2)   # 1.96\n',
        'z_beta   = norm.ppf(power)          # 0.84\n\n',
        'n_required = int(np.ceil(2 * ((z_alpha2 + z_beta) / effect_size) ** 2))\n',
        'print(f"Required n per group: {n_required}")\n',
        'print(f"(Effect size = {effect_size} SD, alpha = {alpha}, power = {power})")\n\n',
        '# Plot power vs. sample size\n',
        'ns = np.arange(10, 500, 5)\n',
        'powers = []\n',
        'for n in ns:\n',
        '    z = effect_size * np.sqrt(n/2) - z_alpha2\n',
        '    powers.append(norm.cdf(z))\n\n',
        'fig, ax = plt.subplots(figsize=(9, 4))\n',
        'ax.plot(ns, powers, color="steelblue", linewidth=2)\n',
        'ax.axhline(0.80, color="red", linestyle="--", label="80% power")\n',
        'ax.axvline(n_required, color="orange", linestyle="--", label=f"n = {n_required}")\n',
        'ax.set_title("Statistical Power vs. Sample Size")\n',
        'ax.set_xlabel("Sample Size (per group)")\n',
        'ax.set_ylabel("Power")\n',
        'ax.legend()\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ['## Summary\n\n',
        '| Concept | Key Formula |\n',
        '|---------|------------|\n',
        '| p-value | P(data as extreme \\| H₀ true) |\n',
        '| t-test | $t = (\\bar{X}_A - \\bar{X}_B) / SE_{diff}$ |\n',
        '| ANOVA F | MSB / MSW |\n',
        r'| Chi-square | $\sum (O-E)^2/E$ |' + '\n',
        '| Power | $P(\\text{reject }H_0 \\mid H_a \\text{ true})$ |\n',
    ])
]

# ─────────────────────────────────────────────────────────────────────────────
# CHAPTER 4 – Regression and Prediction
# ─────────────────────────────────────────────────────────────────────────────
ch4_cells = [
    nb_cell('markdown', [
        '<a href="https://colab.research.google.com/github/Lianaulya/Practical-Statistics-for-Data-Scientists/'
        'blob/main/Chapter4_Regression.ipynb" target="_parent">'
        '<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'
    ]),
    nb_cell('markdown', ['# Chapter 4 – Regression and Prediction\n',
        '**Book:** *Practical Statistics for Data Scientists* (O\'Reilly)\n\n',
        'Topics:\n',
        '- Simple Linear Regression\n',
        '- Multiple Linear Regression\n',
        '- Evaluating Regression: R², RMSE, Residuals\n',
        '- Cross-Validation\n',
        '- Weighted Regression\n',
        '- Prediction vs. Confidence Intervals\n',
        '- Categorical (Dummy) Variables\n',
        '- Multicollinearity & VIF\n',
        '- Confounding Variables\n',
        '- Polynomial and Spline Regression\n'
    ]),
    nb_cell('code', [
        '%matplotlib inline\n\n',
        'import numpy as np\n',
        'import pandas as pd\n',
        'import matplotlib.pyplot as plt\n',
        'import seaborn as sns\n',
        'from scipy import stats\n',
        'from sklearn.linear_model import LinearRegression\n',
        'from sklearn.model_selection import cross_val_score\n',
        'from sklearn.metrics import mean_squared_error\n',
        'import statsmodels.api as sm\n',
        'import statsmodels.formula.api as smf\n\n',
        'BASE_DATA = "https://raw.githubusercontent.com/gedeck/practical-statistics-for-data-scientists/master/data"\n',
        'print("Libraries loaded!")'
    ]),
    nb_cell('markdown', ['## 1. Simple Linear Regression\n\n',
        'Simple linear regression fits a straight line $\\hat{y} = b_0 + b_1 x$\n',
        'that minimizes the **sum of squared residuals (RSS)**:\n\n',
        r'$$RSS = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2 = \sum_{i=1}^{n}(y_i - b_0 - b_1 x_i)^2$$' + '\n\n',
        'The OLS (Ordinary Least Squares) solution:\n\n',
        r'$$b_1 = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sum(x_i - \bar{x})^2} \qquad b_0 = \bar{y} - b_1\bar{x}$$'
    ]),
    nb_cell('code', [
        '# Lung disease data: PEFR vs. exposure to dust\n',
        'lung = pd.read_csv(f"{BASE_DATA}/LungDisease.csv")\n',
        'print(lung.head())\n',
        'print(lung.describe())'
    ]),
    nb_cell('code', [
        '# Fit simple linear regression using statsmodels\n',
        'model_simple = smf.ols("PEFR ~ Exposure", data=lung).fit()\n',
        'print(model_simple.summary())'
    ]),
    nb_cell('code', [
        '# Plot regression line\n',
        'fig, ax = plt.subplots(figsize=(8, 5))\n',
        'ax.scatter(lung["Exposure"], lung["PEFR"], alpha=0.6, color="steelblue", label="Data")\n',
        'x_range = np.linspace(lung["Exposure"].min(), lung["Exposure"].max(), 100)\n',
        'y_pred = model_simple.params[0] + model_simple.params[1] * x_range\n',
        'ax.plot(x_range, y_pred, color="red", linewidth=2,\n',
        '        label=f"OLS: PEFR = {model_simple.params[0]:.1f} + {model_simple.params[1]:.2f}·Exposure")\n',
        'ax.set_title("Lung Disease — PEFR vs. Dust Exposure")\n',
        'ax.set_xlabel("Years of Exposure")\n',
        'ax.set_ylabel("PEFR (L/min)")\n',
        'ax.legend()\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ['## 2. Multiple Linear Regression\n\n',
        'With $p$ predictors:\n\n',
        r'$$\hat{y} = b_0 + b_1 x_1 + b_2 x_2 + \cdots + b_p x_p$$' + '\n\n',
        'In matrix form: $\\hat{\\mathbf{y}} = \\mathbf{X}\\hat{\\boldsymbol{\\beta}}$\n\n',
        'OLS solution: $\\hat{\\boldsymbol{\\beta}} = (\\mathbf{X}^\\top\\mathbf{X})^{-1}\\mathbf{X}^\\top\\mathbf{y}$'
    ]),
    nb_cell('code', [
        '# King County house sales\n',
        'house = pd.read_csv(f"{BASE_DATA}/house_sales.csv", sep="\\t")\n',
        'print(f"Shape: {house.shape}")\n',
        'print(house.head())'
    ]),
    nb_cell('code', [
        '# Multiple regression: price ~ sqft + bedrooms + bathrooms + floors + ...\n',
        'features = ["SqFtTotLiving", "SqFtLot", "Bathrooms", "Bedrooms", "BldgGrade"]\n',
        'X = house[features]\n',
        'y = house["AdjSalePrice"]\n\n',
        'model_multi = smf.ols(\n',
        '    "AdjSalePrice ~ SqFtTotLiving + SqFtLot + Bathrooms + Bedrooms + BldgGrade",\n',
        '    data=house\n',
        ').fit()\n',
        'print(model_multi.summary().tables[1])'
    ]),
    nb_cell('markdown', ['## 3. Evaluating Regression: R², RMSE, and Residuals\n\n',
        '**$R^2$ (Coefficient of Determination):** fraction of variance explained by the model.\n\n',
        r'$$R^2 = 1 - \frac{RSS}{TSS} = 1 - \frac{\sum(y_i-\hat{y}_i)^2}{\sum(y_i-\bar{y})^2}$$' + '\n\n',
        '**RMSE (Root Mean Squared Error):**\n\n',
        r'$$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$$' + '\n\n',
        '**Residual Analysis:** residuals $e_i = y_i - \\hat{y}_i$ should be:\n',
        '- Approximately normally distributed\n',
        '- Homoscedastic (constant variance)\n',
        '- Uncorrelated with predictors\n'
    ]),
    nb_cell('code', [
        '# R² and RMSE\n',
        'y_pred = model_multi.predict(house[features])\n',
        'residuals = y - y_pred\n',
        'rmse = np.sqrt(mean_squared_error(y, y_pred))\n\n',
        'print(f"R²:   {model_multi.rsquared:.4f}")\n',
        'print(f"RMSE: ${rmse:,.0f}")'
    ]),
    nb_cell('code', [
        '# Residual plots\n',
        'fig, axes = plt.subplots(1, 2, figsize=(13, 5))\n\n',
        '# Residuals vs. Fitted\n',
        'axes[0].scatter(y_pred, residuals, alpha=0.3, color="steelblue", s=10)\n',
        'axes[0].axhline(0, color="red", linewidth=1.5)\n',
        'axes[0].set_title("Residuals vs. Fitted Values")\n',
        'axes[0].set_xlabel("Fitted Values ($)")\n',
        'axes[0].set_ylabel("Residuals ($)")\n\n',
        '# Histogram of residuals\n',
        'pd.Series(residuals).hist(bins=40, ax=axes[1], color="steelblue", edgecolor="black")\n',
        'axes[1].set_title("Distribution of Residuals")\n',
        'axes[1].set_xlabel("Residual ($)")\n\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ['## 4. Cross-Validation\n\n',
        '**K-Fold Cross-Validation** is used to estimate out-of-sample model performance:\n',
        '1. Split data into $K$ equal folds\n',
        '2. For each fold: train on $K-1$ folds, evaluate on the held-out fold\n',
        '3. Average the $K$ performance metrics\n\n',
        'This avoids overfitting to training data.'
    ]),
    nb_cell('code', [
        '# 5-fold cross-validation with sklearn\n',
        'from sklearn.linear_model import LinearRegression\n',
        'from sklearn.model_selection import KFold\n',
        'from sklearn.metrics import mean_squared_error\n\n',
        'house_clean = house[features + ["AdjSalePrice"]].dropna()\n',
        'X_cv = house_clean[features].values\n',
        'y_cv = house_clean["AdjSalePrice"].values\n\n',
        'lr = LinearRegression()\n',
        'kf = KFold(n_splits=5, shuffle=True, random_state=42)\n\n',
        'rmse_scores = []\n',
        'r2_scores = []\n',
        'for train_idx, test_idx in kf.split(X_cv):\n',
        '    lr.fit(X_cv[train_idx], y_cv[train_idx])\n',
        '    preds = lr.predict(X_cv[test_idx])\n',
        '    rmse_scores.append(np.sqrt(mean_squared_error(y_cv[test_idx], preds)))\n',
        '    ss_res = np.sum((y_cv[test_idx] - preds)**2)\n',
        '    ss_tot = np.sum((y_cv[test_idx] - y_cv[test_idx].mean())**2)\n',
        '    r2_scores.append(1 - ss_res/ss_tot)\n\n',
        'print(f"5-Fold CV RMSE: ${np.mean(rmse_scores):,.0f} ± ${np.std(rmse_scores):,.0f}")\n',
        'print(f"5-Fold CV R²:   {np.mean(r2_scores):.4f} ± {np.std(r2_scores):.4f}")'
    ]),
    nb_cell('markdown', ['## 5. Categorical Variables (Dummy Encoding)\n\n',
        'Categorical predictors are encoded as **dummy (indicator) variables**.\n',
        'For a categorical variable with $k$ levels, we create $k-1$ binary columns\n',
        'to avoid perfect multicollinearity (the "dummy variable trap").'
    ]),
    nb_cell('code', [
        '# Add property type as dummy variable\n',
        'house2 = house[features + ["PropertyType", "AdjSalePrice"]].dropna().copy()\n',
        'print("Property Types:", house2["PropertyType"].unique())\n\n',
        '# One-hot encoding\n',
        'dummies = pd.get_dummies(house2["PropertyType"], drop_first=True)\n',
        'print("Dummy columns:", list(dummies.columns))\n',
        'house2 = pd.concat([house2, dummies], axis=1)\n',
        'print(house2.head())'
    ]),
    nb_cell('code', [
        '# Regression with categorical variable\n',
        'formula = ("AdjSalePrice ~ SqFtTotLiving + SqFtLot + Bathrooms + Bedrooms"\n',
        '           " + BldgGrade + C(PropertyType)")\n',
        'model_cat = smf.ols(formula, data=house2).fit()\n',
        'print(model_cat.summary().tables[1])\n',
        'print(f"\\nWith PropertyType → R² = {model_cat.rsquared:.4f}")'
    ]),
    nb_cell('markdown', ['## 6. Multicollinearity and VIF\n\n',
        '**Multicollinearity** occurs when predictors are highly correlated.\n',
        'It inflates standard errors and makes coefficients unstable.\n\n',
        '**Variance Inflation Factor (VIF)**:\n\n',
        r'$$VIF_j = \frac{1}{1 - R^2_j}$$' + '\n\n',
        'where $R^2_j$ is obtained by regressing $x_j$ on all other predictors.\n',
        '- $VIF \\approx 1$: no multicollinearity\n',
        '- $VIF > 5$ (or 10): problematic multicollinearity\n'
    ]),
    nb_cell('code', [
        '# Compute VIF for the house price model\n',
        'from statsmodels.stats.outliers_influence import variance_inflation_factor\n\n',
        'X_vif = house_clean[features].assign(const=1)\n',
        'vif_data = pd.DataFrame()\n',
        'vif_data["Feature"] = features\n',
        'vif_data["VIF"] = [variance_inflation_factor(X_vif.values, i) for i in range(len(features))]\n',
        'print(vif_data.sort_values("VIF", ascending=False).to_string(index=False))'
    ]),
    nb_cell('markdown', ['## 7. Polynomial and Spline Regression\n\n',
        '**Polynomial regression** adds polynomial terms to capture non-linear relationships:\n\n',
        r'$$\hat{y} = b_0 + b_1 x + b_2 x^2 + \cdots + b_d x^d$$' + '\n\n',
        '**Spline regression** fits piecewise polynomials joined at **knot points**,\n',
        'allowing more flexible curves without extreme values at the edges.'
    ]),
    nb_cell('code', [
        '# Polynomial regression: house price vs. living area\n',
        'from numpy.polynomial.polynomial import polyfit\n\n',
        'house_small = house_clean.sample(3000, random_state=42)\n',
        'x = house_small["SqFtTotLiving"].values\n',
        'y_h = house_small["AdjSalePrice"].values\n\n',
        'fig, axes = plt.subplots(1, 2, figsize=(14, 5))\n\n',
        'for ax, degree, color in zip(axes, [1, 3], ["red", "green"]):\n',
        '    ax.scatter(x, y_h, alpha=0.15, s=10, color="steelblue")\n',
        '    coeffs = np.polyfit(x, y_h, degree)\n',
        '    x_line = np.linspace(x.min(), x.max(), 200)\n',
        '    y_line = np.polyval(coeffs, x_line)\n',
        '    ax.plot(x_line, y_line, color=color, linewidth=2,\n',
        '            label=f"Degree-{degree} polynomial")\n',
        '    ax.set_title(f"Polynomial Regression (degree={degree})")\n',
        '    ax.set_xlabel("SqFt Living Area")\n',
        '    ax.set_ylabel("Sale Price ($)")\n',
        '    ax.legend()\n\n',
        'plt.tight_layout()\n',
        'plt.show()'
    ]),
    nb_cell('markdown', ['## Summary\n\n',
        '| Concept | Key Formula |\n',
        '|---------|------------|\n',
        '| Simple OLS | $\\hat{y} = b_0 + b_1 x$ |\n',
        '| Multiple OLS | $\\hat{\\mathbf{y}} = \\mathbf{X}\\hat{\\boldsymbol{\\beta}}$ |\n',
        r'| R² | $1 - RSS/TSS$ |' + '\n',
        r'| RMSE | $\sqrt{MSE}$ |' + '\n',
        '| CV | K-fold out-of-sample evaluation |\n',
        r'| VIF | $1/(1-R^2_j)$ — multicollinearity |\n',
    ])
]

# ─────────────────────────────────────────────────────────────────────────────
# Save notebooks
# ─────────────────────────────────────────────────────────────────────────────
nb_configs = [
    ("Chapter1_EDA.ipynb", ch1_cells),
    ("Chapter2_SamplingDistributions.ipynb", ch2_cells),
    ("Chapter3_StatisticalExperiments.ipynb", ch3_cells),
    ("Chapter4_Regression.ipynb", ch4_cells),
]

for fname, cells in nb_configs:
    nb = notebook(cells)
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    print(f"✓ {fname} written ({len(cells)} cells)")

print("\nAll 4 notebooks created successfully!")
