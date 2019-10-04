# RT_List

This is a script to take some of those [RottenTomatoes](https://rottentomatoes.com/) "Top ###"" lists and generate a CSV file that can be imported into a [Letterboxd](https://letterboxd.com) list.

For example, the [RottenTomatoes 140 Best 2010s Horror Movies](https://editorial.rottentomatoes.com/guide/best-2010s-horror-movies/)list will generate the following [Letterboxd List](https://letterboxd.com/alvarop/list/rottentomatoes-140-best-2010s-horror-movies/)

## Instructions
This python script has two dependencies: **requests** and **bs4**. I like using [pipenv](https://github.com/pypa/pipenv) to manage my virtual environments, so to use, you first do `pipenv install` to set up the environment and download the dependencies.

To run the script, do `pipenv run ./rt_list.py <rottentomatoes-list-URL> > output_file.csv`

You can then go to [Letterboxd](https://letterboxd.com), click on create a new list, and import your CSV. You will need a [Letterboxd PRO](https://letterboxd.com/about/pro/) account to do the CSV import. It's only $19/year and you get to support an awesome site!
