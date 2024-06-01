using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MainMenu : MonoBehaviour
{
    public GameObject OptionsPanel;  // Reference to the Options Panel
    public GameObject MainMenuCanvas; // Reference to the Main Menu Canvas

    public void PlayGame()
    {
        SceneManager.LoadScene("GameScene"); // Ensure "GameScene" is the name of your main game scene
    }

    public void QuitGame()
    {
        Application.Quit();
    }

    public void OpenOptions()
    {
        OptionsPanel.SetActive(true);
        MainMenuCanvas.SetActive(false);
    }

    public void CloseOptions()
    {
        OptionsPanel.SetActive(false);
        MainMenuCanvas.SetActive(true);
    }
}
