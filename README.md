# 🚖  Car Sales Dataset Advanced Visualization Dashboard

This academic project is a multi-part interactive dashboard series that explores car sales trends and key product segmentation. Using real-world-style data, I built a set of web-based tools to help users better understand patterns in vehicle features, buyer preferences, and market trends.

Each lab builds on the previous one, starting with simple charts and growing into full dashboards with dynamic filters, clustering, and linked visualizations. These tools are designed to help users ask deeper questions and get quick, visual answers from the data, whether or not if they’re marketing teams, analysts, or business leaders.

### WEBSITE: https://lindy932.github.io/carsales_dashboard/

### What I did: 
- Turn raw data into clear, useful visuals

- Build interactive dashboards using web tools like D3.js

- Use Python to perform data analysis techniques like clustering and trend exploration

- Make complex information easy to explore for any user

Keywords: Python, Product Segmentation, Machine Learning 

---


## 🔍 Key Insights

* **Fuel efficiency drops as car weight increases**
  Curb weight shows a strong negative correlation with highway MPG across all models. Heavier cars are consistently less fuel-efficient.

* **Cylinder count strongly reflects car class**

  * 4-cylinder cars are lightweight, highly fuel-efficient, and tightly clustered.
  * 6-cylinder cars balance power and efficiency.
  * 8-cylinder cars are large, high-performance, but fuel-consuming.

* **Horsepower significantly impacts pricing**
  There's a clear upward trend in price as horsepower increases across all body types.

  * Sedans have the steepest slope which indicates higher price per horse power.
  * Hatchbacks have the shallowest slope which indicates practical and budget-friendly option.

* **Clustering reveals distinct vehicle segments**
  K-Means clustering identifies 4 main groups:

  * Compact, efficient cars
  * Balanced midsize models
  * High-performance, large vehicles (e.g., SUVs)
  * Variants in between
    Car height emerges as a key feature differentiating these groups.

* **High-priced cars prioritize efficiency-focused design**
  Vehicles in the top price tier tend to have taller builds, smaller dimensions, lower curb weight, and higher MPG.
  Lower-priced cars are longer, wider, and less fuel-efficient.

* **Drive type is specialized by body style**
  Sedans and wagons almost exclusively use front-wheel drive, indicating a strong design intent for urban/suburban use with better fuel control and handling.

## 💼 Business Actions

* **Target 4-cylinder models** to fuel-conscious, urban buyers.
* **Price sedans at a premium** for higher horsepower value.
* **Market hatchbacks** as cost-effective, practical options.
* **Segment inventory** using cluster insights to match buyer personas.
* **Highlight FWD sedans and wagons** for city-focused marketing.
* **Use weight and height patterns** to guide pricing and design decisions.

---

### 🚗 **Lab 1 – Exploratory Car Sales Dashboard: Basic Categorical & Numerical Analysis**

- Developed an interactive web dashboard using D3.js to explore relationships between car sales variables through scatterplots, bar charts, and histograms. Enabled users to compare categorical and numerical attributes (e.g., engine size, gender, color) to identify patterns in consumer behavior and vehicle characteristics. Designed dropdown filters and tooltips for enhanced data exploration.
  
<p align="center">
  <img width="390" height="608" alt="Screen Shot 2025-07-31 at 1 25 28 AM" src="https://github.com/user-attachments/assets/aaa999c5-2a6a-4641-b533-8f6c93d1c88d" />
</p>

---

### 📊 **Lab 2 – Product Segmentation and Dimensional Reduction: PCA, MDS & Parallel Coordinates**

- Built a web-based analytical interface to uncover deeper multivariate relationships in the car sales dataset. Implemented correlation matrices, scatterplot matrices, parallel coordinate plots, Principal Component Analysis (PCA) with scree plots and biplots, and Multidimensional Scaling (MDS) displays. Empowered users to visually analyze feature interdependencies and reduce dimensionality for better insights. Data was cleaned, standardized, and clustered using Python, with processed CSVs generated advanced visual analyses.
<p align="center"><img width="231" height="362" alt="Screen Shot 2025-07-31 at 1 25 47 AM" src="https://github.com/user-attachments/assets/3a32d965-f14b-4772-8492-ace7e6189543" /></p>
<p align="center"><img width="327" height="340" alt="Screen Shot 2025-07-31 at 1 25 58 AM" src="https://github.com/user-attachments/assets/4dfdcdc2-aa79-43a3-938b-2a945eef5ca2" /></p>

### Key Insights & Business Relevance

#### 1. **Curb Weight is a Key Driver of Efficiency and Performance**

* **Curb weight** shows **strong negative correlation** with:

  * **Highway MPG** (-0.83)
  * **Engine Size** (-0.78)
  * **Car Length** (-0.69)
* **Why it matters**: Heavier cars tend to consume more fuel and have larger engines—important for aligning sales strategies with customer preferences for fuel efficiency vs. performance.
* **Business Action**: Market lighter vehicles to fuel-conscious buyers; promote heavier models as premium/high-performance options.



#### 2. **Structural Features Are Interconnected**

* **Wheelbase** and **Car Length** show a **strong positive correlation** (+0.89)
* **Car Width** and **Curb Weight** also positively correlated (+0.81)
* **Why it matters**: Understanding the design interdependencies helps segment cars into size classes and plan showroom layouts or highlight car types in digital listings.
* **Business Action**: Offer bundled promotions for larger cars to buyers seeking family vehicles or performance packages.



#### 3. **Drive Type Influences Design**

* Cars with **RWD (rear-wheel drive)** tend to have **higher wheelbases**, averaging **\~105 inches vs. \~98 inches** for other types.
* **Why it matters**: RWD vehicles may appeal more to customers seeking luxury or sports performance.
* **Business Action**: Segment and upsell RWD vehicles as premium options; highlight stability and performance in marketing copy.



#### 4. **Cluster of Economy Cars Identified via PCA**

* PCA plot shows a distinct **cluster of cars in the lower spectrum of PC1 and PC2**, representing:

  * **Lower engine size (< 2.0L)**
  * **Lower horsepower (< 110 HP)**
  * **Lower curb weight (< 2,800 lbs)**
* **Why it matters**: These cars likely represent fuel-efficient, budget-friendly models.
* **Business Action**: Position these models for urban, eco-conscious, or first-time buyers; design promotions around affordability and low maintenance.



#### 5. **High-Performance Features Align in PCA Biplot**

* Biplot loading vectors point in the same direction for:

  * **Horsepower, Curb Weight, Engine Size, Wheelbase**
* Indicates these attributes **collectively define performance-oriented cars**.
* **Why it matters**: Recognizing this trait cluster helps identify and promote high-margin, high-performance vehicles.
* **Business Action**: Create premium performance packages and target performance-focused buyers with aligned offerings.



#### Takeaways 

We can:

* **Segment and promote inventory** based on performance, efficiency, or design preference.
* **Customize sales approaches** to match customer needs (e.g., family car vs. sport vs. economy).
* **Boost revenue** by aligning product positioning with data-backed trends in buyer behavior.


---

### 📌 **Lab 3 – K-Means Clustering Dashboard with Dynamic Filtering**
- Developed a coordinated dashboard where clicking on a specific category in a bar chart assigns a unique legend color and highlights matching data points across all other charts. This interactivity helps users quickly spot trends, compare clusters, and better understand how variables relate to one another in a connected view.

- Designed an interactive clustering tool using K-Means to segment car buyers and vehicle preferences. Integrated adjustable cluster counts and real-time filtering based on key variables (e.g., price, horsepower, MPG). Visualized cluster separation via scatterplots and centroids to support data-driven marketing strategies and customer segmentation. Data was cleaned, standardized, and clustered through the use of Python, with processed CSVs generated for advanced visual analyses.

<p align="center"><img width="329" height="762" alt="Screen Shot 2025-07-31 at 1 26 26 AM" src="https://github.com/user-attachments/assets/97402e7a-2262-4eb0-a0ac-41c4f8658de5" /></p>

## Insights

* **1. 4-cylinder cars** are **highly clustered** and show:

  * **Higher highway MPG**
  * **Lower curb weight, engine size, horsepower**
  * **Tightly grouped in scatterplots and PCA space**, indicating consistency
    - *Ideal for marketing as fuel-efficient and budget-friendly models*

* **6-cylinder cars**:

  * Fall into **mid-range** across performance and size attributes
    - *Balance of efficiency and performance which might be attractive for mainstream buyers*

* **8-cylinder cars**:

  * **High curb weight, horsepower, engine size**
  * **Low highway MPG**
    - *Targeted to performance-oriented buyers, but have fuel trade-offs*



### **2. Car Price Observations (Bar Chart & Parallel Coordinates)**

* **High-priced vehicles** tend to have:

  * **Higher highway MPG**, **taller height**
  * **Smaller length/width**, **lower curb weight**
    - *Reflects consumer preference for lightweight, efficient, modern designs*

* **Low-priced vehicles**:

  * **High wheelbase, length, width**, but **low horsepower & MPG**
   - *May indicate older, bulkier models with outdated performance specs*



### **3. K-Means Clustering (4 Clusters Identified using Elbow Method)**

* **Cluster 0 (Red):**

  * **Low engine size, horsepower, curb weight**
  * **High highway MPG**
    - *Fuel-efficient, compact models*

* **Cluster 2 (Blue):**

  * **High car height**, **engine size**, **horsepower**
  * **Low MPG**
    - *Large SUVs/heavy vehicles — high performance, low efficiency*

* **Cluster 1 & 3 (Green & Orange):**

  * **Moderate across most variables**
   - *Well-balanced vehicles appealing to average consumers*

* **Distinct separation in MDS plot** confirms clustering strength



### 4. Cross-Attribute Trends & Design Trade-Offs

* **Inverse relationship** between:

  * **Performance metrics** (engine size, horsepower)
  * **Fuel efficiency** (highway MPG)

* **Car height**:

  * Longest loading vector in biplot
  * Main driver of variation across clusters
  * Taller cars → more powerful, less efficient
  * Shorter cars → more efficient, compact
   - *Clear design trade-off: Power & space vs. efficiency*

---

### **Takeaways**

* **Tailor marketing by vehicle type**:

  * Fuel-efficient compacts (Cluster 0) → budget-conscious urban drivers
  * High-performance large cars (Cluster 2) → premium buyers or off-road markets

* **Use cluster profiles to guide inventory and pricing strategy**:

  * Promote fuel efficiency in eco-conscious regions
  * Price higher for feature-rich tall/performance models despite fuel trade-offs

* **Highlight clear vehicle trade-offs to match consumer priorities**:

  * Performance vs. fuel savings
  * Size/space vs. compact urban use

---


### 📈 **Lab 4 – Linked Car Sales Dashboard Suite: Coordinated Multiple Views**

-  Created an interconnected dashboard system with four synchronized visualizations (scatterplots, bar charts, pie charts, and histograms). Enabled dynamic linking—changing filters in one chart automatically updated all others. Focused on visual storytelling of car sales trends across variables like income, fuel type, transmission, and company to support executive-level data exploration. Data was cleaned, standardized, and clustered through the use of Python, with processed CSVs generated for advanced visual analyses.
  
-  **Note:** Press Shift Key to De-Select and Multi-Select Variables 
<p align="center"><img width="1365" height="716" alt="Screen Shot 2025-07-31 at 1 26 49 AM" src="https://github.com/user-attachments/assets/96b84bf7-9a98-43c4-aebb-cfecdec66294" /></p>

## Data Story 1: **Horsepower vs. Price by Car Body Type**

* **Consistent Positive Trend**:

  * Across all car body types, there is a **strong linear relationship** between **horsepower** and **price**.
  * ➤ *Higher-performing cars tend to command higher prices across the market.*

* **Slope Comparison Reveals Pricing Strategies**:

  * **Sedans** have a **steeper slope** than other body types.

    * ➤ *Indicates a higher price premium per unit increase in horsepower.*
  * **Hatchbacks** show the **shallowest slope**.

    * ➤ *Suggests that horsepower has less pricing power in this body segment, favoring practicality and affordability.*

### Insights

* **Market Behavior**:

  * Horsepower is a **universal pricing factor**—regardless of car body, performance metrics drive value.

* **Pricing Strategy**:

  * **Dynamic pricing models** can be developed:

    * Sedans: *Market as premium, performance-driven choices.*
    * Hatchbacks: *Market for cost-effectiveness and utility.*

* **Market Segmentation **:

  * Use slope differences to identify **consumer expectations by car type**—performance vs. practicality.

## Data Story 2: **Drive Wheel Type vs. Car Body Style (Chord Diagram)**

* **Distinct Pairing of Drive Type and Body Style**:

  * **Sedan** and **wagon** body types show strong associations with **front-wheel drive (FWD)**.
  * These two body types **do not overlap** with other drive types (e.g., RWD, 4WD).

* **Unique Self-Contained Relationships**:

  * ➤ *FWD is a defining characteristic for sedans and wagons in this dataset.*

* **Contextual Insight**:

  * FWD sedans are ideal for **urban/suburban** areas, offering **better fuel economy** and **lower maintenance**—important where cost of living is high.

### Insights

* **Manufacturer Strategy**:

  * Car makers deliberately pair FWD with sedans/wagons to meet **city-driver needs** (fuel savings, efficiency).

* **Market Advantage**:

  * The **non-overlapping nature** of FWD in these body types creates **product distinctiveness**.

    * ➤ *Opportunity to market FWD sedans as the go-to choice for urban commuters.*
    * ➤ *Strategically differentiate against competitors in SUV or RWD-heavy segments.*

* **Market Research**:

  * These patterns help identify **untapped or underserved niches**, guiding both **product design** and **targeted advertising**.


---

