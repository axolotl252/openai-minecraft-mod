package com.jbm11208.autosocial.mixin.client;

import com.jbm11208.autosocial.AutoSocialLogic;
import net.minecraft.client.gui.components.ChatComponent;
import net.minecraft.network.chat.Component;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

@Mixin(ChatComponent.class)
public class ChatHudMixin {
    @Inject(method = "addMessage(Lnet/minecraft/network/chat/Component;)V", at = @At("TAIL"))
    private void autosocial_onAddMessage(Component message, CallbackInfo ci) {
        AutoSocialLogic.init();
        AutoSocialLogic.onChat(message);
    }
}
