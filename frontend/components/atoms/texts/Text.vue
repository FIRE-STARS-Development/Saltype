<script setup lang="ts">
interface Props {
  color?: "white" | "black" | "blue" | "dark-blue";
  size?: "small" | "medium" | "large";
  text?: string;
}

const props = withDefaults(defineProps<Props>(), {
  color: "white",
  size: "medium",
  text: "テキスト",
});
</script>

<template>
  <p :class="[`text--${props.color}`, `text--${props.size}`]">
    {{ props.text }}
  </p>
</template>

<style lang="scss" src="@/assets/styles/components/atoms/text.scss" />
