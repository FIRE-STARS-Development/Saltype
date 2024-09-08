<script setup lang="ts">
interface Props {
  type?: string;
  id?: string;
  modelValue?: string | boolean;
  placeholder?: string;
  required?: boolean;
  color?: "white" | "black" | "blue" | "dark-blue";
  border?: "white" | "black" | "blue" | "dark-blue" | "none";
  width?: "small" | "medium" | "large";
  height?: "small" | "medium" | "large";
  background?: "white" | "black" | "blue" | "dark-blue";
  rounded?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
  type: "text",
  id: "default",
  required: false,
  color: "white",
  border: "none",
  width: "medium",
  height: "medium",
  background: "black",
  rounded: false,
});

defineEmits(["update:modelValue"]);
</script>

<template>
  <input
    :type="`${props.type}`"
    :id="`${props.id}`"
    :value="modelValue"
    :name="`${props.id}`"
    :placeholder="`${props.placeholder}`"
    :required="props.required"
    @input="
      $emit('update:modelValue', ($event.target as HTMLInputElement).value)
    "
    :class="[
      `input-text--${props.color}`,
      `input-border--${props.border}`,
      `input-width--${props.width}`,
      `input-height--${props.height}`,
      `input-background--${props.background}`,
      { 'input--rounded': props.rounded },
    ]"
  />
</template>

<style lang="scss" src="@/assets/styles/components/atoms/input.scss" />
