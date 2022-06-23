SET timezone = 'Asia/Singapore';

CREATE TABLE IF NOT EXISTS COUNTRY_VACCINATIONS (
  country VARCHAR(250) NOT NULL,
  iso_code VARCHAR(10) NOT NULL,
  vacc_date DATE,
  total_vaccinations DECIMAL,
  people_vaccinated DECIMAL,
  people_fully_vaccinated DECIMAL,
  daily_vaccinations_raw DECIMAL,
  daily_vaccinations DECIMAL,
  total_vaccinations_per_hundred DECIMAL,
  people_vaccinated_per_hundred DECIMAL,
  people_fully_vaccinated_per_hundred DECIMAL,
  daily_vaccinations_per_million DECIMAL,
  vaccines VARCHAR(250),
  source_name VARCHAR(250),
  source_website VARCHAR(250)
);

