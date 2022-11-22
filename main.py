from helper import *

import streamlit as st

import os

st.title('Restaurant success Classifier')

st.title("Features")

listed_in_type_options = ['Buffet', 'Cafes', 'Delivery', 'Desserts', 'Dine-out',
                          'Drinks & nightlife', 'Pubs and bars']
listed_in_city_options = ['BTM',
                          'Banashankari',
                          'Bannerghatta Road',
                          'Basavanagudi',
                          'Bellandur',
                          'Brigade Road',
                          'Brookefield',
                          'Church Street',
                          'Electronic City',
                          'Frazer Town',
                          'HSR',
                          'Indiranagar',
                          'JP Nagar',
                          'Jayanagar',
                          'Kalyan Nagar',
                          'Kammanahalli',
                          'Koramangala 4th Block',
                          'Koramangala 5th Block',
                          'Koramangala 6th Block',
                          'Koramangala 7th Block',
                          'Lavelle Road',
                          'MG Road',
                          'Malleshwaram',
                          'Marathahalli',
                          'New BEL Road',
                          'Old Airport Road',
                          'Rajajinagar',
                          'Residency Road',
                          'Sarjapur Road',
                          'Whitefield']

location_options = ['Banashankari', 'Basavanagudi', 'Mysore Road', 'Jayanagar',
                    'Kumaraswamy Layout', 'Rajarajeshwari Nagar', 'Vijay Nagar',
                    'Uttarahalli', 'JP Nagar', 'South Bangalore', 'City Market',
                    'Nagarbhavi', 'Bannerghatta Road', 'BTM', 'Kanakapura Road',
                    'Bommanahalli', 'CV Raman Nagar', 'Electronic City', 'HSR',
                    'Marathahalli', 'Sarjapur Road', 'Wilson Garden', 'Shanti Nagar',
                    'Koramangala 5th Block', 'Koramangala 8th Block', 'Richmond Road',
                    'Koramangala 7th Block', 'Jalahalli', 'Koramangala 4th Block',
                    'Bellandur', 'Whitefield', 'East Bangalore', 'Old Airport Road',
                    'Indiranagar', 'Koramangala 1st Block', 'Frazer Town', 'RT Nagar',
                    'MG Road', 'Brigade Road', 'Lavelle Road', 'Church Street',
                    'Ulsoor', 'Residency Road', 'Shivajinagar', 'Infantry Road',
                    'St. Marks Road', 'Cunningham Road', 'Race Course Road',
                    'Commercial Street', 'Vasanth Nagar', 'HBR Layout', 'Domlur',
                    'Ejipura', 'Jeevan Bhima Nagar', 'Old Madras Road', 'Malleshwaram',
                    'Seshadripuram', 'Kammanahalli', 'Koramangala 6th Block',
                    'Majestic', 'Langford Town', 'Central Bangalore', 'Sanjay Nagar',
                    'Brookefield', 'ITPL Main Road, Whitefield',
                    'Varthur Main Road, Whitefield', 'KR Puram',
                    'Koramangala 2nd Block', 'Koramangala 3rd Block', 'Koramangala',
                    'Hosur Road', 'Rajajinagar', 'Banaswadi', 'North Bangalore',
                    'Nagawara', 'Hennur', 'Kalyan Nagar', 'New BEL Road', 'Jakkur',
                    'Rammurthy Nagar', 'Thippasandra', 'Kaggadasapura', 'Hebbal',
                    'Kengeri', 'Sankey Road', 'Sadashiv Nagar', 'Basaveshwara Nagar',
                    'Yeshwantpur', 'West Bangalore', 'Magadi Road', 'Yelahanka',
                    'Sahakara Nagar', 'Peenya']

rest_type_options = ['Bakery',
                     'Bar',
                     'Beverage Shop',
                     'Bhojanalya',
                     'Cafe',
                     'Casual Dining',
                     'Club',
                     'Confectionery',
                     'Delivery',
                     'Dessert Parlor',
                     'Dhaba',
                     'Fine Dining',
                     'Food Court',
                     'Food Truck',
                     'Irani Cafee',
                     'Kiosk',
                     'Lounge',
                     'Meat Shop',
                     'Mess',
                     'Microbrewery',
                     'Pub',
                     'Quick Bites',
                     'Sweet Shop',
                     'Takeaway']
# Pop Up
cuisines_options = ['Afghan',
                    'Afghani',
                    'African',
                    'American',
                    'Andhra',
                    'Arabian',
                    'Asian',
                    'Assamese',
                    'Australian',
                    'Awadhi',
                    'BBQ',
                    'Bakery',
                    'Bar Food',
                    'Belgian',
                    'Bengali',
                    'Beverages',
                    'Bihari',
                    'Biryani',
                    'Bohri',
                    'British',
                    'Bubble Tea',
                    'Burger',
                    'Burmese',
                    'Cafe',
                    'Cantonese',
                    'Charcoal Chicken',
                    'Chettinad',
                    'Chinese',
                    'Coffee',
                    'Continental',
                    'Desserts',
                    'Drinks Only',
                    'European',
                    'Fast Food',
                    'Finger Food',
                    'French',
                    'German',
                    'Goan',
                    'Greek',
                    'Grill',
                    'Gujarati',
                    'Healthy Food',
                    'Hot dogs',
                    'Hyderabadi',
                    'Ice Cream',
                    'Indian',
                    'Indonesian',
                    'Iranian',
                    'Italian',
                    'Japanese',
                    'Jewish',
                    'Juices',
                    'Kashmiri',
                    'Kebab',
                    'Kerala',
                    'Konkan',
                    'Korean',
                    'Lebanese',
                    'Lucknowi',
                    'Maharashtrian',
                    'Malaysian',
                    'Mangalorean',
                    'Mediterranean',
                    'Mexican',
                    'Middle Eastern',
                    'Mithai',
                    'Modern Indian',
                    'Momos',
                    'Mongolian',
                    'Mughlai',
                    'Naga',
                    'Nepalese',
                    'North Eastern',
                    'North Indian',
                    'Oriya',
                    'Paan',
                    'Pan Asian',
                    'Parsi',
                    'Pizza',
                    'Portuguese',
                    'Rajasthani',
                    'Raw Meats',
                    'Roast Chicken',
                    'Rolls',
                    'Russian',
                    'Salad',
                    'Sandwich',
                    'Seafood',
                    'Sindhi',
                    'Singaporean',
                    'South American',
                    'South Indian',
                    'Spanish',
                    'Sri Lankan',
                    'Steak',
                    'Street Food',
                    'Sushi',
                    'Tamil',
                    'Tea',
                    'Tex-Mex',
                    'Thai',
                    'Tibetan',
                    'Turkish',
                    'Vegan',
                    'Vietnamese',
                    'Wraps']

book_table = st.radio("Can book Table?", ["Yes", "No"])
online_order = st.radio("Supports online order", ["Yes", "No"])
votes = int(st.number_input("Number of votes"))
# location = st.selectbox("Location", location_options)
rest_type = st.multiselect("Restaurant type", rest_type_options)
cuisines = st.multiselect("Cuisines", cuisines_options)
approx_cost = st.number_input("Approximate cost(for two people)")
listed_in_type = st.selectbox("Listed in(type)", listed_in_type_options)
listed_in_city = st.selectbox("Listed in(city)", listed_in_city_options)


def predict(online_order, book_table, votes, approx_cost, listed_in_type, listed_in_city, rest_type, cuisines):
    online_order, book_table = reformatData(online_order, book_table)
    number_of_cuisines = len(cuisines)
    listed_in_type_data = createListedInTypeData(listed_in_type)
    listed_in_city_data = createListedInCityData(listed_in_city)
    rest_type_data = createRestTypeData(rest_type)
    cuisines_data = createCuisinesData(cuisines)

    data = [online_order, book_table, votes, approx_cost,
            number_of_cuisines] + listed_in_type_data + listed_in_city_data + rest_type_data + cuisines_data
    # print("data len22 ", len(data))
    st.title("This restaurant will be " + predictor([data])[0])


def createListedInTypeData(listed_in_type_value):
    listed_in_type_index = listed_in_type_options.index(listed_in_type_value)
    list_data = [0] * len(listed_in_type_options)
    list_data[listed_in_type_index] = 1
    return list_data


def createListedInCityData(listed_in_city_value):
    listed_in_city_index = listed_in_city_options.index(listed_in_city_value)
    list_data = [0] * len(listed_in_city_options)
    list_data[listed_in_city_index] = 1
    return list_data


def createRestTypeData(rest_type_list):
    list_data = [0] * len(rest_type_options)
    for val in rest_type_list:
        rest_type_index = rest_type_options.index(val)
        list_data[rest_type_index] = 1
    return list_data


def createCuisinesData(Cuisines_list):
    list_data = [0] * len(cuisines_options)
    for val in Cuisines_list:
        cuisine_index = cuisines_options.index(val)
        list_data[cuisine_index] = 1
    return list_data


def reformatData(online_order_value, book_table_value):
    if book_table_value == "Yes":
        book_table_value = 1
    else:
        book_table_value = 0

    if online_order_value == "Yes":
        online_order_value = 1
    else:
        online_order_value = 0
    return online_order_value, book_table_value


predict = st.button("Predict",
                    on_click=predict(online_order, book_table, votes, approx_cost, listed_in_type, listed_in_city,
                                     rest_type, cuisines))
