import axios from 'axios';

const API_URL = 'http://localhost:5000';

export const fetchCityData = async (cityName) => {
  try {
    const response = await axios.get(`${API_URL}/api/city/${cityName}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching city data:', error);
    throw error;
  }
};