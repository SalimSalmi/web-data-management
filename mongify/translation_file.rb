table "acted_in" do
    column "idacted_in", :key
    column "idmovies", :integer , :references => :movies
    column "idseries", :integer
    column "idactors", :integer, :references => :actors
    column "character", :string
    column "billing_position", :integer
end

table "actors" do
    column "idactors", :key
    column "lname", :string
    column "fname", :string
    column "mname", :string
    column "gender", :integer
    column "number", :integer
end

table "aka_names", :ignore => true


table "aka_titles", :ignore => true


table "keywords", :ignore => true


table "movies" do
    column "idmovies", :key
    column "title", :string
    column "year", :integer
    column "number", :integer
    column "type", :integer
    column "location", :string
    column "language", :string
end

table "movies_genres" do
    column "idmovies_genres", :key
    column "idmovies", :integer , :references => :movies
    column "idgenres", :integer , :references => :genres
    column "idseries", :integer
end

table "movies_keywords", :ignore => true

table "series", :ignore => true

table "genres" do
    column "idgenres", :key
    column "genre", :integer
end
