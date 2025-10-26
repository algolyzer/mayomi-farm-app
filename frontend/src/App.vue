<template>
  <div id="app" class="min-h-screen flex flex-col">
    <!-- Navigation -->
    <nav class="bg-white shadow-lg sticky top-0 z-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-20">
          <!-- Logo -->
          <router-link to="/" class="flex items-center space-x-3">
            <div class="text-4xl">🌾</div>
            <div>
              <h1 class="text-xl md:text-2xl font-bold gradient-text font-bengali">মায়োমি নিশাত</h1>
              <p class="text-xs md:text-sm text-gray-600">এগ্রো ফার্ম</p>
            </div>
          </router-link>

          <!-- Desktop Menu -->
          <div class="hidden md:flex items-center space-x-8">
            <router-link 
              to="/" 
              class="nav-link font-bengali text-gray-700 hover:text-primary-600 transition-colors font-medium"
              active-class="text-primary-600"
            >
              প্রথম পাতা
            </router-link>
            <router-link 
              to="/products" 
              class="nav-link font-bengali text-gray-700 hover:text-primary-600 transition-colors font-medium"
              active-class="text-primary-600"
            >
              পণ্য
            </router-link>
            <router-link 
              to="/about" 
              class="nav-link font-bengali text-gray-700 hover:text-primary-600 transition-colors font-medium"
              active-class="text-primary-600"
            >
              আমাদের সম্পর্কে
            </router-link>
            <router-link 
              to="/contact" 
              class="nav-link font-bengali text-gray-700 hover:text-primary-600 transition-colors font-medium"
              active-class="text-primary-600"
            >
              যোগাযোগ
            </router-link>
            <a href="tel:+8801711727357" class="btn-primary text-sm">
              📞 কল করুন
            </a>
          </div>

          <!-- Mobile Menu Button -->
          <button 
            @click="mobileMenuOpen = !mobileMenuOpen" 
            class="md:hidden text-gray-700 focus:outline-none"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
              <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <!-- Mobile Menu -->
        <div v-show="mobileMenuOpen" class="md:hidden pb-4">
          <router-link 
            to="/" 
            class="block py-2 font-bengali text-gray-700 hover:text-primary-600"
            @click="mobileMenuOpen = false"
          >
            প্রথম পাতা
          </router-link>
          <router-link 
            to="/products" 
            class="block py-2 font-bengali text-gray-700 hover:text-primary-600"
            @click="mobileMenuOpen = false"
          >
            পণ্য
          </router-link>
          <router-link 
            to="/about" 
            class="block py-2 font-bengali text-gray-700 hover:text-primary-600"
            @click="mobileMenuOpen = false"
          >
            আমাদের সম্পর্কে
          </router-link>
          <router-link 
            to="/contact" 
            class="block py-2 font-bengali text-gray-700 hover:text-primary-600"
            @click="mobileMenuOpen = false"
          >
            যোগাযোগ
          </router-link>
          <a href="tel:+8801711727357" class="block py-2 font-bengali text-primary-600 font-semibold">
            📞 কল করুন
          </a>
        </div>
      </div>
    </nav>

    <!-- Main Content -->
    <main class="flex-grow">
      <router-view />
    </main>

    <!-- Footer -->
    <footer class="gradient-bg text-white py-12">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- About -->
          <div>
            <h3 class="text-2xl font-bold mb-4 font-bengali">মায়োমি নিশাত এগ্রো ফার্ম</h3>
            <p class="text-green-100 font-bengali">প্রকৃতির ছোঁয়ায়, মানসম্মত কৃষি উৎপাদনে একটি বিশ্বাসযোগ্য নাম।</p>
          </div>

          <!-- Quick Links -->
          <div>
            <h4 class="text-lg font-semibold mb-4 font-bengali">দ্রুত লিংক</h4>
            <ul class="space-y-2 font-bengali">
              <li><router-link to="/" class="text-green-100 hover:text-white transition-colors">প্রথম পাতা</router-link></li>
              <li><router-link to="/products" class="text-green-100 hover:text-white transition-colors">পণ্য</router-link></li>
              <li><router-link to="/about" class="text-green-100 hover:text-white transition-colors">আমাদের সম্পর্কে</router-link></li>
              <li><router-link to="/contact" class="text-green-100 hover:text-white transition-colors">যোগাযোগ</router-link></li>
            </ul>
          </div>

          <!-- Contact Info -->
          <div>
            <h4 class="text-lg font-semibold mb-4 font-bengali">যোগাযোগ</h4>
            <ul class="space-y-2 text-green-100 font-bengali">
              <li>📍 Vabakhali bazar</li>
              <li>📞 <a href="tel:+8801711727357" class="hover:text-white transition-colors">+8801711727357</a></li>
              <li>📧 <a href="mailto:nishat@manishatagro.com" class="hover:text-white transition-colors">nishat@manishatagro.com</a></li>
            </ul>
          </div>
        </div>

        <div class="border-t border-green-600 mt-8 pt-8 text-center text-green-100 font-bengali">
          <p>&copy; 2025 মায়োমি নিশাত এগ্রো ফার্ম। সর্বস্বত্ব সংরক্ষিত।</p>
        </div>
      </div>
    </footer>

    <!-- Chatbot Button -->
    <button 
      @click="chatbotOpen = !chatbotOpen"
      class="fixed bottom-6 right-6 w-16 h-16 bg-primary-600 text-white rounded-full shadow-2xl hover:bg-primary-700 transition-all duration-300 z-50 flex items-center justify-center text-2xl hover:scale-110"
    >
      <span v-if="!chatbotOpen">💬</span>
      <span v-else>✕</span>
    </button>

    <!-- Chatbot Window -->
    <transition name="slide-up">
      <div 
        v-if="chatbotOpen" 
        class="fixed bottom-24 right-6 w-96 max-w-[calc(100vw-3rem)] bg-white rounded-2xl shadow-2xl z-50 flex flex-col"
        style="height: 500px; max-height: calc(100vh - 200px);"
      >
        <!-- Chatbot Header -->
        <div class="gradient-bg text-white p-4 rounded-t-2xl">
          <h3 class="text-lg font-bold font-bengali">🤖 চ্যাটবট সহায়তা</h3>
          <p class="text-sm text-green-100 font-bengali">আমরা আপনাকে সাহায্য করতে এখানে আছি</p>
        </div>

        <!-- Chat Messages -->
        <div class="flex-grow overflow-y-auto p-4 space-y-3 bg-gray-50">
          <div v-for="(msg, index) in chatMessages" :key="index">
            <!-- User Message -->
            <div v-if="msg.type === 'user'" class="flex justify-end">
              <div class="bg-primary-600 text-white rounded-lg px-4 py-2 max-w-[80%] font-bengali">
                {{ msg.text }}
              </div>
            </div>
            <!-- Bot Message -->
            <div v-else class="flex justify-start">
              <div class="bg-white border border-gray-200 rounded-lg px-4 py-2 max-w-[80%] font-bengali">
                {{ msg.text }}
              </div>
            </div>
          </div>
        </div>

        <!-- Chat Input -->
        <div class="p-4 border-t">
          <form @submit.prevent="sendMessage" class="flex space-x-2">
            <input 
              v-model="chatInput"
              type="text" 
              placeholder="আপনার বার্তা লিখুন..."
              class="flex-grow px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 font-bengali"
            />
            <button 
              type="submit"
              class="bg-primary-600 text-white px-6 py-2 rounded-lg hover:bg-primary-700 transition-colors font-bengali"
            >
              পাঠান
            </button>
          </form>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      mobileMenuOpen: false,
      chatbotOpen: false,
      chatInput: '',
      chatMessages: [
        {
          type: 'bot',
          text: 'আসসালামু আলাইকুম! মায়োমি নিশাত এগ্রো ফার্মে আপনাকে স্বাগতম। আমি আপনাকে কীভাবে সাহায্য করতে পারি?'
        }
      ]
    }
  },
  methods: {
    async sendMessage() {
      if (!this.chatInput.trim()) return

      // Add user message
      this.chatMessages.push({
        type: 'user',
        text: this.chatInput
      })

      const userMessage = this.chatInput
      this.chatInput = ''

      try {
        // Send to API
        const response = await axios.post('/api/chat', {
          message: userMessage
        })

        // Add bot response
        this.chatMessages.push({
          type: 'bot',
          text: response.data.response
        })
      } catch (error) {
        console.error('Chat error:', error)
        this.chatMessages.push({
          type: 'bot',
          text: 'দুঃখিত, একটি সমস্যা হয়েছে। অনুগ্রহ করে আবার চেষ্টা করুন।'
        })
      }

      // Scroll to bottom
      this.$nextTick(() => {
        const chatContainer = document.querySelector('.overflow-y-auto')
        if (chatContainer) {
          chatContainer.scrollTop = chatContainer.scrollHeight
        }
      })
    }
  }
}
</script>

<style scoped>
.slide-up-enter-active,
.slide-up-leave-active {
  transition: all 0.3s ease;
}

.slide-up-enter-from {
  transform: translateY(100%);
  opacity: 0;
}

.slide-up-leave-to {
  transform: translateY(100%);
  opacity: 0;
}
</style>
