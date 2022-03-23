package main

import (
  "math/rand"
  "net/http"
  "encoding/json"
)

func main() {
  http.HandleFunc("/healthz", health)
  http.HandleFunc("/random/number", randomNumber)

  http.ListenAndServe(":5000", nil)
}

type healthResponse struct {
  Healthy bool `json:"healthy"`
}

type randomNumberResponse struct {
  Location string `json:"location"`
  Number int `json:"number"`
  EndpointVersion string `json:"endpoint_version"`
}

func health(w http.ResponseWriter, req *http.Request) {
  json.NewEncoder(w).Encode(&healthResponse{
    Healthy: true,
  })
}

func randomNumber(w http.ResponseWriter, req *http.Request) {
  w.WriteHeader(http.StatusInternalServerError)
  json.NewEncoder(w).Encode(&randomNumberResponse{
    Location: "/random/number",
    Number: nil,
    EndpointVersion: "v2",
  })
}
