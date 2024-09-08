<script setup lang="ts">
interface Props {
  type?: "button" | "submit" | "reset";
  buttonText?: string;
  color?: "white" | "black" | "blue" | "dark-blue";
  border?: "white" | "black" | "blue" | "dark-blue" | "none";
  width?: "small" | "medium" | "large" | "same-as-input-large";
  height?: "small" | "medium" | "large";
  background?: "white" | "black" | "blue" | "dark-blue";
  rounded?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
  type: "button",
  color: "white",
  border: "none",
  width: "medium",
  height: "medium",
  background: "black",
  rounded: false,
});
</script>

<template>
  <button
    :type="`${props.type}`"
    :class="[
      `button-text--${props.color}`,
      `button-border--${props.border}`,
      `button-width--${props.width}`,
      `button-height--${props.height}`,
      `button-background--${props.background}`,
      { 'button--rounded': props.rounded },
    ]"
  >
    <slot name="any" />
    {{ props.buttonText }}
  </button>
</template>

<style lang="scss" src="@/assets/styles/components/atoms/button.scss" />
