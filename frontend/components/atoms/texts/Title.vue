<script setup lang="ts">
interface Props {
  color?: "white" | "black" | "blue" | "dark-blue";
  size?: "small" | "medium" | "large";
  text?: string;
}

const props = withDefaults(defineProps<Props>(), {
  color: "white",
  size: "medium",
  text: "見出し",
});
</script>

<template>
  <h1 :class="[`title--${props.color}`, `title--${props.size}`]">
    {{ props.text }}
  </h1>
</template>

<style lang="scss" src="@/assets/styles/components/atoms/title.scss" />
