# Pandas_VS_Polars

Polars is designed for high-performance data manipulation and is particularly useful for large datasets, while Pandas is more commonly used in the Python ecosystem for general data analysis tasks.

| Aspect                   | Polars                               | Pandas                               |
|--------------------------|-------------------------------------|--------------------------------------|
| **Language**             | Rust with Python bindings            | Python                               |
| **Performance**          | Designed for high performance       | Slower for large datasets in Python   |
| **Data Model**           | Immutable data model                | Mutable data model                   |
| **API Design**           | Performance-focused API with Pandas compatibility | Comprehensive and user-friendly API |
| **Integration**          | Growing integration in Python       | Well-integrated into Python ecosystem |
| **Community & Ecosystem** | Smaller user base, benefits from Rust ecosystem | Large and active user community      |

![Pandas Result](https://github.com/TiwariLaxuu/Pandas_VS_Polars/blob/main/pandas_result.png)
![Polar Result](https://github.com/TiwariLaxuu/Pandas_VS_Polars/blob/main/polar_result.png)


Polars is also very lightweight. It comes with zero required dependencies, and this shows in the import times:

polars: 70ms
numpy: 104ms
pandas: 520ms

In the TPCH benchmarks polars is orders of magnitudes faster than pandas, dask, modin and vaex on full queries (including IO).

**References** 

![Reference 1](https://pandas.pydata.org/)
![Reference 2](https://www.pola.rs/)
