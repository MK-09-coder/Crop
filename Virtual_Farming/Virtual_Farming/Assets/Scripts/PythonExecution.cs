using UnityEngine;
using System.Diagnostics;
using System.Threading.Tasks;
using System;
using Debug = UnityEngine.Debug;

public class PythonExecution : MonoBehaviour
{
    [Serializable]
    public class UserInput
    {
        public string pH;
        public string Water_Depth;
        public string Temperature;
        public string Fertilizer;
        public string Organic_Matter_Content;
        public string Moisture_Content_at_Harvest;
    }

   

    [Serializable]
    public class MyData
    {
        public UserInput user_input;
        public string[] bot_reply;
    }

    private MyData data;
    public TextAsset dJson;

    private async void Start()
    {
        await ExecutePythonScriptAsync(@"E:\Crop\Virtual_Farming\Virtual_Farming\Assets\Scripts\crop.py");
        ReadJson();
    }
    private void ReadJson()
    {
        
            data = JsonUtility.FromJson<MyData>(dJson.text);
            Debug.Log("pH: " + data.user_input.pH);
            Debug.Log("Water Depth: " + data.user_input.Water_Depth);
            Debug.Log("Temperature: " + data.user_input.Temperature);
            Debug.Log("Fertilizer: " + data.user_input.Fertilizer);
            Debug.Log("Organic Matter Content: " + data.user_input.Organic_Matter_Content);
            Debug.Log("Moisture Content at Harvest: " + data.user_input.Moisture_Content_at_Harvest);

            foreach (string reply in data.bot_reply)
            {
                Debug.Log("Bot Reply: " + reply);
            }
        
    }
    private async Task ExecutePythonScriptAsync(string scriptPath)
    {
        Process process = new Process();
        process.StartInfo.FileName = @"C:\Users\B02\AppData\Local\Microsoft\WindowsApps\python.exe"; // Replace with the path to your Python interpreter if necessary
        process.StartInfo.Arguments = scriptPath;
        process.StartInfo.UseShellExecute = false;
        process.StartInfo.RedirectStandardOutput = true;
        process.StartInfo.RedirectStandardError = true;
        process.StartInfo.CreateNoWindow = true;

        process.Start();
        process.BeginOutputReadLine();
        process.BeginErrorReadLine();

        await Task.Run(() =>
        {
            process.WaitForExit();
        });

        process.Close();
        Debug.Log("Executed");
    }
}
