﻿using HarmonyLib;
using System.Collections;
using System.Reflection;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace NeonLite.Modules.Optimization
{
    internal class FastStart : IModule
    {
#pragma warning disable CS0414
        const bool priority = true;
        static bool active = false;

        static bool preload = false;

        internal static AsyncOperation audioPreload;
        internal static AsyncOperation menuPreload;
        internal static AsyncOperation enemyPreload;

        static void Setup()
        {
            var setting = Settings.Add(Settings.h, "Misc", "fastStart", "Fast Startup", "Preloads essential scenes before the game even initializes to speed up the menu load.", true);
            setting.OnEntryValueChanged.Subscribe((_, after) => Activate(after));
            active = setting.Value;

            //MelonCoroutines.Start(PreloadCoroutine());
        }

        static IEnumerator PreloadCoroutine() {
            Preload();
            yield return null;
        }

        static readonly MethodInfo loadon = AccessTools.Method(typeof(Setup), "Start");
        static readonly MethodInfo ogstate = AccessTools.Method(typeof(Game), "SetInitializationState");
        static readonly MethodInfo ogdata = AccessTools.Method(typeof(Game), "OnGameDataLoaded");

        static void Activate(bool activate)
        {
            if (activate)
            {
                NeonLite.Harmony.Patch(loadon, prefix: Helpers.HM(Preload));
                NeonLite.Harmony.Patch(ogstate, prefix: Helpers.HM(SetInitState));
                NeonLite.Harmony.Patch(ogdata, prefix: Helpers.HM(UnloadScenesRewrite));
            }
            else
            {
                NeonLite.Harmony.Unpatch(loadon, Helpers.MI(Preload));
                NeonLite.Harmony.Unpatch(ogstate, Helpers.MI(SetInitState));
                NeonLite.Harmony.Unpatch(ogdata, Helpers.MI(UnloadScenesRewrite));
            }

            active = activate;
        }

        static void Preload()
        {
            if (preload) 
                return;
            NeonLite.LoadAssetBundle();
            preload = true;
            NeonLite.Logger.Msg("Started scene preload, please wait...!");
            menuPreload = SceneManager.LoadSceneAsync("MenuHolder", LoadSceneMode.Additive);
            enemyPreload = SceneManager.LoadSceneAsync("Enemies", LoadSceneMode.Additive);
            audioPreload = SceneManager.LoadSceneAsync("Audio", LoadSceneMode.Additive);
        }

        static void RemoveFrontload(ref bool enforceMinimumTime, ref bool frontloadWait) => enforceMinimumTime = frontloadWait = false;
        static bool SetInitState(Game __instance, int initializationState, ref int ____initializationState)
        {
            if (NeonLite.DEBUG)
                NeonLite.Logger.Msg($"SetInitState {initializationState}");

            if (initializationState == 2)
            {
                Singleton<GameInput>.Instance.Initialize();
                ____initializationState = 3;
                if (menuPreload.isDone)
                    ____initializationState = 4;
                else
                    menuPreload.completed += _ => AccessTools.Field(typeof(Game), "_initializationState").SetValue(__instance, 4);
                return false;
            }
            return initializationState > ____initializationState;
        }
        static bool UnloadScenesRewrite(Game __instance, ref int ____initializationState)
        {
            GameDataManager.ApplyShadowPrefs();
            if (audioPreload.isDone)
                ____initializationState = 8;
            else
                audioPreload.completed += _ => AccessTools.Field(typeof(Game), "_initializationState").SetValue(__instance, 8);
            return false;
        }
    }
}
