package com.jbm11208.autosocial;

import net.fabricmc.api.ClientModInitializer;

public class AutoSocialClient implements ClientModInitializer {

    @Override
    public void onInitializeClient() {
        System.out.println("[AutoSocial] Client mod initialized.");
        // Mixins will trigger logic on first chat message.
    }
}
