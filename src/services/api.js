import axios from "axios";

export default axios.create({
  // baseURL: "http://104.198.244.0:8123/",
  baseURL: "http://165.227.62.217/",
  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
  },
});
