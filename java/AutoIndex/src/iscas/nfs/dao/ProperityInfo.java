package iscas.nfs.dao;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class ProperityInfo {
	private static Properties config = null;
	public static final String DATABASE_FILENAME = "DB.properties";

	/**
	 * @param null
	 * @return Properties from the .properties
	 * @Discribe ��ȡ.Properties(�����ļ�) ��Ϣ,�൱��һ�����ݶ���洢��̬����
	 */
	public static Properties getProperties() {
		if (config == null) {
			config = new Properties();
			InputStream in = ProperityInfo.class.getClassLoader()
					.getResourceAsStream(DATABASE_FILENAME);
			try {
				config.load(in);
				System.out.println(" Config load success!");
				return config;
			} catch (IOException e) {
				e.printStackTrace();
			}
		} else {
			return config;
		}
		return null;
	}
}
