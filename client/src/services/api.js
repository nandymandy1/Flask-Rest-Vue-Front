import axios from "axios";
import { HOST } from "../Constants";

const BaseURL = HOST;

let headers = {
  "Content-Type": "application/json"
};

/**
 * @Dec This function will make all types of the POST Request
 */
export const postData = async (url, fields) => {
  try {
    // let res = await axios.post(BaseURL + url, fields, { headers });
    let { data } = await axios.post(BaseURL + url, fields, { headers });
    return data;
  } catch (err) {
    return err.response.data;
  }
};

/**
 * @Dec This function will make all types of the GET Request
 */
export const getData = async url => {
  try {
    let { data } = await axios.get(BaseURL + url, { headers });
    return data;
  } catch (err) {
    return err.response.data;
  }
};
