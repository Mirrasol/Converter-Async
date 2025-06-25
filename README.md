
Currency Converter - a simple and easy to use REST API to check the latest global currency rates. It provides registered users with an access to the list of world currencies and allows them to convert from one currency to another. The project includes JWT authentication and integration with an external API for a real-time exchange.

## Features

  - register and login to check the list of all available currencies
  - quickly convert one currency to another using the most recent exchange rate data

## Installation

This project is built using FastAPI as the main framework. Please refer to the pyproject.toml file for the full list of required dependencies.

1) Download the package from GitHub:

`git clone git@github.com:Mirrasol/Currency-Converter.git`

2) Install using uv from your console:

`make install`

or set your own virtual environment using pip and other package managers.

3) Don't for get to create the .env file that contains your secret keys and database settings. Please refer to '.env_example'.


Note: you can get the API_Key from the external forex API: ["Currency Data API"](https://apilayer.com/marketplace/currency_data-api`).

4) Run the project with a command: using Uvicorn:

`make run`

or with a Uvicorn directly:

`uvicorn main:app`

5) Check Makefile for the rest of the available commands.

## List of endpoints

![](/img/endpoints.png)

## Swagger Demo Screens

- Registering new user:

![](/img/2_register.png)

- Successful response:

![](img/3_register_response.png)

-  Login request:

![](img/4_login.png)

- Login response:

![](img/5_login_response.png)

- Getting the list of currencies:

![](img/6_curr_list.png)
![](img/7_curr_list_response.png)

- Checking exchange:

![](img/8_exchange.png)
![](img/9_exchange_response.png)
