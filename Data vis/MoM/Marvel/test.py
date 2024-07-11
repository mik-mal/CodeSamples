import polars as pl
import polars.selectors as cs
from great_tables import GT, md
from great_tables import nanoplot_options

df = pl.read_csv("./movie_data.csv")



res = (
    df.with_columns(
        (pl.col("category").str.to_lowercase() + ".png").alias("icon"),
        (pl.col("budget")*1000000),
        (pl.col("worldwide_gross")*1000000),
        (pl.col("budget_recovered")*100),
        (pl.col("critics_score")*-1)
    )
    .select("icon", "film", "budget", "worldwide_gross", "budget_recovered", "critics_score", "audience_score","year")
    )



res2 = res.sort(["icon", "year"]).select("icon", "film", "budget", "worldwide_gross", "budget_recovered", "critics_score", "audience_score")

(
    GT(res2, rowname_col="icon")
    
    .fmt_nanoplot(
        columns="worldwide_gross", 
        plot_type="bar",
        options = nanoplot_options(
            data_bar_fill_color = "#504a4a",
            data_bar_stroke_color = "#504a4a")
    )
    .fmt_nanoplot(
        columns="budget", 
        plot_type="bar",
        options = nanoplot_options(
            data_bar_fill_color = "#518cca",
            data_bar_stroke_color = "#518cca")
    )
    .fmt_nanoplot(
        columns="budget_recovered", 
        plot_type="bar",
        options = nanoplot_options(
            data_bar_fill_color = "#f78f3f",
            data_bar_stroke_color = "#f78f3f")
    )
    .fmt_nanoplot(
        columns="critics_score", 
        plot_type="line",
        options = nanoplot_options(
            data_line_stroke_color = "#E23636",
            data_point_fill_color = "#E23636")
    )

    .fmt_nanoplot(
        columns="audience_score", 
        plot_type="line",
        options = nanoplot_options(
            data_line_stroke_color = "#000000",
            data_point_fill_color = "#000000")
    )
    
    .tab_header("MCU earnings and movie ratings")
    
    .tab_spanner(
        label ="Earnings", 
        columns=["worldwide_gross", "budget", "budget_recovered"])
    
    .tab_spanner("Movie Ratings", cs.contains("score"))

    .cols_label(**{
        "worldwide_gross": "Worldwide Gross $",
        "budget": "Budget $",
        "budget_recovered": "% Budget Recovered",
        "film": "Film",
        "critics_score": "Critics",
        "audience_score": "Audience"
    })

    .fmt_image("icon", path="./")
    .tab_source_note(
        md(
            '<br><div style="text-align: center;">'
            "Data: Information is Beautiful/Makeover Monday"
            "</div>"
            "<br>"
        )
    )
    .save(
        "marvel.png",
        scale = 1,
        expand = 500,
        window_size= (12000,12000)
    )
)

