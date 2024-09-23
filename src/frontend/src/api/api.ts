export const fetchPredictions = async (crypto: string, modelType: string) => {
    const response = await fetch(`/predict/${crypto}/${modelType}`);
    return await response.json();
  };
  