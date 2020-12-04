vector<int> z_algo(string s) { //空文字列に注意!!
	int c=0, n=s.size();
	vector<int> z(n, 0);
	for (int i=1; i<n; i++) {
		int l = i-c;
		if (i+z[l]<c+z[c]) z[i] = z[l];
		else {
			int j = max(0, c+z[c]-i);
			while (i+j<n && s[j]==s[i+j]) j++;
			z[i] = j;
			c = i;
		}
	}
    z[0] = n;
	return z;
}