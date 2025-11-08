package com.jbm11208.autosocial;

import net.fabricmc.api.ClientModInitializer;
import net.fabricmc.fabric.api.client.event.lifecycle.v1.ClientTickEvents;
import net.fabricmc.fabric.api.client.keybinding.v1.KeyBindingHelper;
import net.minecraft.client.KeyMapping;
import org.lwjgl.glfw.GLFW;

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;

public class ClientKeybinds implements ClientModInitializer {

    private static KeyMapping skipKey;
    private static KeyMapping reloadConfigKey;

    @Override
    public void onInitializeClient() {
        System.out.println("[AutoSocial] ClientKeybinds initializing...");
        // Register keybinding for skipping current audio; appears in Controls -> Key Binds
        skipKey = KeyBindingHelper.registerKeyBinding(createKeyMapping("key.autosocial.skip", GLFW.GLFW_KEY_UNKNOWN, "key.categories.misc"));
        // Register keybinding for reloading config
        reloadConfigKey = KeyBindingHelper.registerKeyBinding(createKeyMapping("key.autosocial.reload_config", GLFW.GLFW_KEY_UNKNOWN, "key.categories.misc"));

        // Listen for key presses each client tick
        ClientTickEvents.END_CLIENT_TICK.register(client -> {
            if (skipKey != null) {
                while (skipKey.consumeClick()) {
                    System.out.println("[AutoSocial] Skip key pressed. Requesting audio skip...");
                    AutoSocialLogic.skipCurrentAudio();
                }
            }
            if (reloadConfigKey != null) {
                while (reloadConfigKey.consumeClick()) {
                    System.out.println("[AutoSocial] Reload Config key pressed. Reloading config.yml...");
                    boolean ok = AutoSocialLogic.reloadConfig();
                    if (client.player != null) {
                        client.player.connection.sendChat("IAMAB0T[AI] Wario: config reload -> " + (ok ? "OK" : "FAILED") + ", model=" + AutoSocialLogic.getModelSafe());
                    }
                }
            }
        });
    }

    private static KeyMapping createKeyMapping(String translationKey, int defaultKey, String categoryKey) {
        try {
            // Prefer Mojang-style constructor: (String, int, String)
            Constructor<KeyMapping> mojangCtor = KeyMapping.class.getConstructor(String.class, int.class, String.class);
            return mojangCtor.newInstance(translationKey, defaultKey, categoryKey);
        } catch (NoSuchMethodException mojangMissing) {
            try {
                // Fallback to enum Category signature: (String, int, KeyMapping.Category)
                Class<?> categoryClass = Class.forName("net.minecraft.client.KeyMapping$Category");
                Field miscField = categoryClass.getField("MISC");
                Object misc = miscField.get(null);
                Constructor<KeyMapping> yarnCtor = KeyMapping.class.getConstructor(String.class, int.class, categoryClass);
                return yarnCtor.newInstance(translationKey, defaultKey, misc);
            } catch (Throwable t) {
                throw new RuntimeException("Failed to construct KeyMapping with either signature", t);
            }
        } catch (Throwable t) {
            throw new RuntimeException("Failed to construct KeyMapping", t);
        }
    }
}
